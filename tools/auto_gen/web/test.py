class TestClass(object):
  val1 = 100
   
  def __init__(self):
    self.val2 = 200
   
  def fcn(self,val = 400):
    val3 = 300
    self.val4 = val
    self.val5 = 500
    
if __name__ == '__main__':
  inst = TestClass()
  inst.fcn(200)
  inst2 = TestClass()  
  inst2.val1 = 3000 
  print inst.val1
  print inst2.val1
  print TestClass.val1

  

