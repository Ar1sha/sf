import pandas as pd
sd = pd.read_csv('D:\sf\Pandas\Students_performance\students_performance.csv', sep=',')
score_mean = sd['reading score'].mean()
mask = sd['test preparation course'] == 'completed'
mask2 = sd['lunch'] == 'standard'
mask3 = sd['lunch'] == 'free/reduced'
mask4 = sd['parental level of education'] == "bachelor's degree"
count_mask4 = sd[mask4 == True].shape[0]
mask5 = sd['race/ethnicity'] == 'group A'
mask6 = sd['race/ethnicity'] == 'group C'
writing_mask_A = sd[mask5==True]['writing score'].median()
writing_mask_C = sd[mask6==True]['writing score'].median()

print(abs(writing_mask_A - writing_mask_C))