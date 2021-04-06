import numpy as np
import matplotlib.pyplot as plt

#Declaring theoritically found pmf of R.V 'X' denoting the number of subjects passed (and finding corresponding cdf)

faces=np.array([1,2,3,4,5,6]) #X takes the following values
print("Number of subjects passed (X) : ",faces)
pmf=np.array([1/21,2/21,3/21,4/21,5/21,6/21]) #pmf of X
print("Theoritical PMF of X : ",pmf)
cdf=np.cumsum(pmf)
print("Theoritical CDF of X : ",cdf)

#Generating samples from the pmf and finding sim_pmf and sim_cdf

num_trials=10000 #Number of samples
U=np.random.rand()
Samples=np.array([])
for i in range(num_trials):
  index=np.count_nonzero(np.random.rand()>=cdf)
  Samples=np.append(Samples,faces[index])
print("The samples are : ",Samples)
sim_pmf=np.zeros(6)
for i in range(6):
  sim_pmf[i]=np.count_nonzero(Samples == (i+1))/num_trials
print("Simulated pmf of X : " , sim_pmf)
sim_cdf=np.cumsum(sim_pmf)
print("Simulated CDF of X : ",sim_cdf)


#Plotting Variations in theoratical and practical outcome 

labels = ['1', '2', '3', '4','5','6']
Theoratical = [1/21,2/21,3/21,4/21,5/21,6/21 ]
Calculated = sim_pmf

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Theoratical, width, label='Theoratical')
rects2 = ax.bar(x + width/2, Calculated, width, label='Practical')

ax.set_ylabel('PMF')
ax.set_xlabel('Faces of the die')
ax.set_title('GATE EC - 8 : Calculated PMF vs Theoratical PMF ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()

labels = ['1', '2', '3', '4','5','6']
Theoratical =  cdf.tolist()
Calculated = sim_cdf

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Theoratical, width, label='Theoratical')
rects2 = ax.bar(x + width/2, Calculated, width, label='Practical')

ax.set_ylabel('CDF ')
ax.set_xlabel('Faces of the die')
ax.set_title('GATE EC - 8 : Calculated CDF vs Theoratical CDF ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()
