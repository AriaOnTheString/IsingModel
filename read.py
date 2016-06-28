 # -*- coding: utf-8 -*-

import cPickle
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('font', family='Arial')  # to display greek letters

yaxis = {'energy': 'Energy per site / J',
         'mag': 'Magnetisation per site',
         'capacity': 'C per site / J^2',
         'chi': 'Chi per site'}  # mapping of y axis type

def betagraph(ytype, xdata, ydata):
  'Graph for varying beta.'
  fig, ax = plt.subplots()
  ax.plot(xdata, ydata, 'r')
  ax.set_xlabel(u'β')
  ax.set_ylabel(yaxis[ytype])
  plt.show()

def fieldgraph(ytype, toposx, toposy, tonegx, tonegy):
  'Graph for varying field.'
  fig, ax = plt.subplots()
  ax.plot(toposx[::-1], toposy, 'r', label='-J to J')
  ax.plot(tonegx, tonegy, 'g', label='J to -J')
  ax.set_xlabel(u'μB')
  ax.set_ylabel(yaxis[ytype])
  ax.legend(loc='upper right', shadow=True)
  plt.show()

def resvarybetanofield():
  'Varying beta, no field.'
  with open('varybetanofield.pkl', 'rb') as resultsdict:
    data = cPickle.load(resultsdict)
  betagraph('energy', data['beta'], [e/625 for e in data['energy']]) # energy per site
  betagraph('mag', data['beta'], data['magnetisation'])
  betagraph('capacity', data['beta'], data['capacity'])
  betagraph('chi', data['beta'], data['susceptibility'])

def resvarybetaposfield():
  'Varying beta, low positive field.'
  with open('varybetaposfield.pkl', 'rb') as resultsdict:
    data = cPickle.load(resultsdict)
  betagraph('energy', data['beta'], [e/625 for e in data['energy']])
  betagraph('mag', data['beta'], data['magnetisation'])
  betagraph('capacity', data['beta'], data['capacity'])
  betagraph('chi', data['beta'], data['susceptibility'])

def resvaryfieldlowtemp():
  'Varying field, low temperature.'
  with open('varyfieldlowtemp.pkl', 'rb') as resultsdict:
    data = cPickle.load(resultsdict)
  fieldgraph('energy', data['npfield'], [e/625 for e in data['npenergy']], data['pnfield'], [e/625 for e in data['pnenergy']])
  fieldgraph('mag', data['npfield'], [-m for m in data['npmagnetisation']], data['pnfield'], data['pnmagnetisation'])
  fieldgraph('capacity', data['npfield'], data['npcapacity'], data['pnfield'], data['pncapacity'])
  fieldgraph('chi', data['npfield'], data['npsusceptibility'], data['pnfield'], data['pnsusceptibility'])

def printmatrix(picklefile, datatype, topos, index):
  'Prints the matrix, given the pickle file and index.'
  with open(picklefile, 'rb') as resultsdict:
    data = cPickle.load(resultsdict)
  if datatype == 'beta':
    string = 'Beta: %s' % data['beta'][index]
    matrix = data['matrixlist'][index]
  else:
    string = 'Field: %s' % data['field'][index]
    if topos == True:
      matrix = data['npmatrixlist'][index]
    elif topos == False:
      matrix = data['pnmatrixlist'][index]

  ax = plt.gca()
  ax.patch.set_facecolor('gray')
  ax.set_aspect('equal', 'box')
  ax.xaxis.set_major_locator(plt.NullLocator())
  ax.yaxis.set_major_locator(plt.NullLocator())

  for (x,y),w in np.ndenumerate(matrix):  # adds squares piecewise
    color = 'black' if w == 1 else 'white'
    rect = plt.Rectangle([x, y], 1, 1, facecolor=color, edgecolor=color)
    ax.add_patch(rect)

  ax.autoscale_view()
  ax.invert_yaxis()
  plt.title(string)
  plt.show()