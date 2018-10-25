class stack:
      def __init__(self):
           self.stack=[]

      def push(self,data):
          self.stack.append(data)

      def pop(self):
          if self.stack.count is not 0 :
              return None
          else :
              return self.stack.pop
      
      def topelement(self):
          if self.stack.count is not 0 :
              return None
          else:
              return self.stack[-1]
      
      def printelement(self):
          if self.stack.count is not 0:
              n = len(self.stack)
              for i in range(0,n):
                  print(self.stack[i])

S = stack()

for i in range(0,10):
    S.push(i)
S.printelement()
    
