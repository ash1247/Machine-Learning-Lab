data <- read.csv(file.choose(), header = TRUE)
print(data)
idx<-sample(1:dim(data)[1],6)
dataSample<-data[idx,]
dataSample$Species<-NULL
hc<-hclust(dist(dataSample),method="ave")
plot(hc,hang=-1,labels=data$Species[idx])
rect.hclust(hc,k=3)
groups<-cutree(hc,k=3)