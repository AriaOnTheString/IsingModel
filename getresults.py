import cPickle
import iterator  # shared object

size = 25

def varybeta(field, size=size):
  'Returns general averaged results for varying beta.'
  betalist = []
  Elist = []
  Clist = []
  Mlist = []
  Chilist = []
  matrixlist = []
  for beta in xrange(0, 101):
    beta *= 0.01
    print 'Beta: %s' % beta
    energy, capacity, mag, chi, matrix = iterator.avgvalues(beta, field, size, 20)
    betalist.append(beta)
    Elist.append(energy)
    Clist.append(capacity)
    Mlist.append(mag)
    Chilist.append(chi)
    matrixlist.append(matrix)
  resultsdict = {'beta':betalist, 'energy':Elist, 'magnetisation':Mlist, 'capacity':Clist, 'susceptibility':Chilist, 'matrixlist':matrixlist}
  return resultsdict

def varyfield(beta, size=size):
  '''
  Returns general averaged results for varying field.
  Positive and negative directions are recorded separately.
  '''
  pnfieldlist = []
  pnElist = []
  pnClist = []
  pnMlist = []
  pnChilist = []
  pnmatrixlist = []
  npfieldlist = []
  npElist = []
  npClist = []
  npMlist = []
  npChilist = []
  npmatrixlist = []
  for field in xrange(100, -101, -1):  # negative direction
    field *= 0.01
    print 'Field: %s' % field
    energy, capacity, mag, chi, matrix = iterator.avgvalues(beta, field, size, 20)
    pnfieldlist.append(field)
    pnElist.append(energy)
    pnClist.append(capacity)
    pnMlist.append(mag)
    pnChilist.append(chi)
    pnmatrixlist.append(matrix)
  for field in xrange(-100, 101):  # positive direction
    field *= 0.01
    print 'Field: %s' % field
    energy, capacity, mag, chi, matrix = iterator.avgvalues(beta, field, size, 20)
    npfieldlist.append(field)
    npElist.append(energy)
    npClist.append(capacity)
    npMlist.append(mag)
    npChilist.append(chi)
    npmatrixlist.append(matrix)
  resultsdict = {'pnfield':pnfieldlist, 'pnenergy':pnElist, 'pnmagnetisation':pnMlist, 'pncapacity':pnClist, 
    'pnsusceptibility':pnChilist, 'pnmatrixlist':pnmatrixlist, 'npfield':npfieldlist, 'npenergy':npElist, 
    'npmagnetisation':npMlist, 'npcapacity':npClist,'npsusceptibility':npChilist, 'npmatrixlist':npmatrixlist}
  return resultsdict

def varybetanofield():
  print "Varying beta, no field."
  resultsdict = varybeta(0.0)
  with open('varybetanofield.pkl', 'wb') as results:
    cPickle.dump(resultsdict, results)

def varybetaposfield():
  print "Varying beta, with positive field."
  resultsdict = varybeta(0.5)
  with open('varybetaposfield.pkl', 'wb') as results:
    cPickle.dump(resultsdict, results)

def varyfieldlowtemp():
  print "Varying field, low temp."
  resultsdict = varyfield(1.0)
  with open('varyfieldlowtemp.pkl', 'wb') as results:
    cPickle.dump(resultsdict, results)