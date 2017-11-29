## Visualization of the change in p-value with increasing sample size ##

install.packages("timeDate")
library(timeDate)
library(ggplot2)

# Actual probability of CTR for each groups
pA = 0.05
pB = 0.05
# Number of cases for each groups
nA = 500
nB = 500

alpha = 0.05


# Simulate Data:
data = data.frame(group = rep(c("A", "B"), c(nA, nB)), 
               timestamp = sample(seq(as.timeDate('2017-01-01'), 
                                      as.timeDate('2017-06-30'), by=1), nA+nB),
               clicked = as.factor(c(sample(rbinom(n=30000, size=1, prob=pA), nA),
                                     sample(rbinom(n=30000, size=1, prob=pA), nB)))
               )

colnames(data)[2] = "time"
data = data[order(data$time), ]

# Compute current p-values after every observation: 
pval = c()
index = c()

for (i in 50:dim(data)[1]){
  contingency = table(data$group[1:i], data$clicked[1:i])
  pval = c(pval, prop.test(contingency)$p.value)
  index = c(index, i)
}
results = data.frame(index = index, pValue = pval) 


# Plot the p-values
ggplot(results, aes(x = index, y = pValue)) + 
  geom_line() + geom_hline(aes(yintercept = alpha)) + 
  scale_y_continuous(name = "p-value", limits = c(0,1)) + 
  scale_x_continuous(name = "Observed data points") + theme(text = element_text(size=12))




##Chi-square test with 95% confidence interval##

library(readr)

# Specify file path: 
dataPath = "https://www.inwt-statistics.de/files/INWT/downloads/exampleDataABtest.csv" 
example = read_csv(file = dataPath)  
str(example)
names(example)[3] = "clicked"

# Change type of varaibles
example$group = as.factor(example$group)
example$clicked = as.factor(example$clicked)  

# Compute frequencies and conduct test for proportions  
# (Frequency table with successes in the first column) 
freqTable <- table(example$group, example$clicked)[, c(2,1)]
freqTable

# Conduct significance test 
prop.test(freqTable, conf.level = .95)


