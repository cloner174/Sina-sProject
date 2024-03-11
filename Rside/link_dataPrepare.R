library(dplyr)

node <- read.csv("data/node_data.csv")

link <- read.csv("~/Documents/Python/mr.Sina/V3.final/Sina-sProject/data/links.csv")

head(link)

node <- as.data.frame(node)
link <- as.data.frame(link)

A <- vector()
B <- vector()

which( link$source == 27 ) 
node$X_igraph_index

node$X_igraph_index

dim(link)[1]

node$X_igraph_index

V <- node$X_igraph_index

VV <- list()
for (i in c(1:702)) {
  VV[[i]] <- which(link$source == V[i] | link$target == V[i])
}


LL <- vector()
for (i in c(1:702)) {
  temp <- VV[[i]]
  for (j in temp) {
    LL <- c(LL, j)
  }
}

link_data <- link[LL,]

link_data

write.csv(link_data, 'link_dataFinal.csv')
write.csv(link_data, 'output/link_dataFinal.csv')
write.csv(link_data, '~/Documents/Python/mr.Sina/V3.final/Sina-sProject/data/link_dataFinal.csv')
