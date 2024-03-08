#
library(conflicted)
library(dplyr)
library(stringr)
#library(tidyr)
#library(tibble)




getwd()
#setwd("Rside/")



publish_content <- read.csv("data/publisher_contents.csv")

#View(publish_content)
#View(adver_camp)
class(publish_content)

colnames(publish_content)
dim(publish_content)





#Start with Smaller!

length(unique(publish_content$ID))
length(unique(publish_content$Total.Likes))
length(unique(publish_content$Total.Views))
length(unique(publish_content$Price))
length(unique(publish_content$Total.Interactions))
length(unique(publish_content$Total.Reach))
length(unique(publish_content$Publisher.Price))
length(unique(publish_content$Media.Plan.Price))
length(unique(publish_content$Has.Paid.Partnership))
length(unique(publish_content$Media.App.Media.Plan...Media.Plan...Content.Type))
length(unique(publish_content$Media.App.Media.Plan...Media.Plan...Campaign.Type))
length(unique(publish_content$Media.App.Media.Plan...Media.Plan...Is.Vip))
length(unique(publish_content$Media.App.Media.Category...Media.Category...ID))
length(unique(publish_content$Media.App.Media...Media...Is.Influencer))
length(unique(publish_content$Media.App.Media...Media...Is.Private))
length(unique(publish_content$Media.App.Media...Media...Is.Celebrity))
length(unique(publish_content$Media.App.Media.Category...Media.Category...Title))

length(unique(publish_content$Media.App.Media...Media...Publisher.ID))




dim(publish_content)

publisherDF <- publish_content %>%
  select( c(ID,Media.App.Media...Media...Publisher.ID,Total.Likes,Total.Views,Price,Total.Interactions,Total.Reach,
            Publisher.Price, Media.Plan.Price, Has.Paid.Partnership, Media.App.Media.Plan...Media.Plan...Content.Type,
            Media.App.Media.Plan...Media.Plan...Campaign.Type,Media.App.Media.Plan...Media.Plan...Is.Vip,
            Media.App.Media.Category...Media.Category...ID, Media.App.Media...Media...Is.Influencer,
            Media.App.Media...Media...Is.Private,Media.App.Media...Media...Is.Celebrity,
            Media.App.Media.Category...Media.Category...Title, Media.App.Media...Media...Publisher.ID) )



dim(publisherDF)


interactions <- read.csv("data/interactions.csv")

advertiserDF <-  read.csv("output/advertiser.csv")



UniqAdertisers <- unique(advertiserDF$Advertiser.ID)



bothpresents <- list()
num_ = 1
for (UniqAdertiser in UniqAdertisers) {
  
  bothpresents[[num_]] <-  which( interactions$Campaign.Campaign...Campaign...Advertiser.ID == UniqAdertiser)
  num_ = num_+1
}

length(bothpresents)



both_present <- vector()

for ( i in c(1:length(bothpresents))) {
  
  for ( j in c(1:length(bothpresents[[i]]))) {
    
    both_present <- c(both_present, bothpresents[[i]][j])
  }
}

length(both_present)

both_present <- na.omit(both_present)

length(both_present)


validus <- interactions$Media.App.Media...Media...Publisher.ID[both_present]

length(validus)

validus <- unique(validus)

length(validus)


finalSteps1 <- list()
num_ = 1
for (i  in validus ) {
  finalSteps1[[num_]] <- ( which( publisherDF$Media.App.Media...Media...Publisher.ID ==  i) )
  num_ = num_ + 1
}


finalSteps2 <- vector()

for ( i in c(1:length(finalSteps1))) {
  
  for ( j in c(1:length(finalSteps1[[i]]))) {
    
    finalSteps2 <- c(finalSteps2, finalSteps1[[i]][j])
  }
}

length(finalSteps2)

finalSteps2 <- na.omit(finalSteps2)

length(finalSteps2)





PublisherDataFrame <- publisherDF[finalSteps2,]

dim(PublisherDataFrame)


ValidsA <- which(PublisherDataFrame$Total.Likes != 0)

PublisherDataFrame <- PublisherDataFrame[ValidsA,]


dim(PublisherDataFrame)




#options("max.print" = 5000)

write.csv(x = PublisherDataFrame , file =  "output/publishers.csv")

#end1