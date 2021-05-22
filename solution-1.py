#jobs : list of jobs
#slots : number of slots
def sequencing (works, slots):
  
  #number of jobs
  n = len(works)
  
  #sort jobs in descending order of profit
  for i in range(n):
    for j in range(n-1-i):
      if works[j][2]<works [j + 1][2]:
        jobs[j], jobs[j + 1] = jobs[j + 1], jobs[j]
        result=[False] * slots
        
  #result
  job = []
        
  #for each job
   for i in range(len(works)):
          
  #find available solt
   for j in range (min(slot - 1,works[i][1]-1),-1, -1)
          
  #solt available
   if reslut[j] is False
     result[j] = True
     job.append(job[i][0])
  break
  print(job)
            
  #test the function
   jobs=[['a',4,20], #jobs
     ['b',1,10],
     ['c',1,40],
     ['d',1,30]] 
     print("the following is the maximun profit sequence of the jobs ")
