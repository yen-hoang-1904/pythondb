def createGenerator():
  mylist = range(3)
  for i in mylist:
    yield (i*i)


def main():
  mlist = createGenerator()
  print(mlist)
  for i in mlist:
    print(i)


  x = ('apple', 'banana', 'strawberry')
  elist = enumerate(x)
  for c, v in elist:
    print(f'{c} -- {v}\n')


  y = ['a', 'b', 'c']
  print(y + ['u'])



if __name__== '__main__':main()
