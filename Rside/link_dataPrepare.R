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


link_data <- link %>%
  filter( source == V | target == V)

link_data

write_csv(link_data, 'link_data.csv')
write_csv(link_data, 'output/link_data.csv')
write_csv(link_data, '~/Documents/Python/mr.Sina/V3.final/Sina-sProject/data/link_data.csv')
