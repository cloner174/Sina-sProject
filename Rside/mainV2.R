
library(readr)
library(conflicted)
library(dplyr)
library(readr)
library(readxl)
library(stringi)
library(stringr)
library(tidyr)
library(tibble)


getwd()
#setwd("Rside/")

adver_camp <- read_csv("data/advertiser_campaigns.csv")
publish_content <- read_csv("data/publisher_contents.csv")

#View(publish_content)
#View(adver_camp)
class(publish_content)
class(adver_camp)

colnames(publish_content)
colnames(adver_camp)
dim(publish_content)
dim(adver_camp)

#Start with Smaller!

#length(unique(adver_camp$`Media Plans Filter → Categories`))
#length(adver_camp$`Media Plans Filter → Categories`)

#uniqCat <- unique(adver_camp$`Media Plans Filter → Categories`)
class(uniqCat)
View(uniqCat)

categori <- adver_camp$`Media Plans Filter → Categories`
class(categori)
categori[1]
#strsplit(x = categori[1], split = "")

cateAll <- vector()
for (i in c( 1 : length(categori) )) {
  temp <- categori[i]
  temp2 <- str_split(temp, boundary("word"))[[1]][4]
  cateAll[i] <- temp2
}

( uniqCateAll <- unique(cateAll) )
uniqCateAll <- na.omit(uniqCateAll)
uniqCateAll
class(uniqCateAll)
length(uniqCateAll)
uniqCateAll[1]
uniqCateAll[40]
uniqCateAll[54]

#tempolar <- list()
#for (i in uniqCateAll) {
#  
#  tempolar[[i]] <- as.vector( which( cateAll == i ) )
#  
#}
#class(tempolar)
#tempolar[[1]]
#tempolar$آشپزی
#adver_camp$ID[tempolar$///////////]



names <- vector()
IDs <- vector()
n <- 0
for (i in c(1: length(uniqCateAll))) {
  k <- uniqCateAll[i]
  K <- as.vector( which( cateAll == k ) )
  for (j in K) {
    jj <- adver_camp$`Advertiser ID`[which(cateAll == j)]
    names <- c(names, k)
    IDs <- c(IDs, jj)
  }
}

( adver_campIDsCategory <- data.frame( cbind( names, IDs)) )

#options("max.print" = 5000)

write_csv(x = adver_campIDsCategory , file =  "output/adver_campIDsCategory.csv")






length(unique(publish_content$`Total Likes`))
length(publish_content$ID)
length(unique(publish_content$`Total Likes`))

unique(publish_content$ID)

uniqPub <- unique(publish_content$ID)
class(uniqPub)
View(uniqPub)

goodlikes <- which( unique(publish_content$`Total Likes`) > 1000 )

NumLiksUpper1000 <- unique(publish_content$`Total Likes`)[goodlikes]

GoodPublisherIDs <- vector()
for (i in NumLiksUpper1000) {
  GoodPublisherIDs <- c(GoodPublisherIDs,
               (publish_content$`Media App Media - Media → Publisher ID`[which( publish_content$`Total Likes` == i)]) )
}

GoodPublisherIDs <- unique(GoodPublisherIDs)

length(GoodPublisherIDs)


unique(publish_content$`Media App Media Plan - Media Plan → Content Type`)
unique(publish_content$`Media App Media Plan - Media Plan → Campaign Type`)
unique(publish_content$`Media App Media Plan - Media Plan → Is Vip`)
unique(publish_content$`Media App Media Plan - Media Plan → Content Format`)
unique(publish_content$`Media App Media Plan - Media Plan → Impression`)
unique(publish_content$`Media App Media Plan - Media Plan → Estimated Reach`)
unique(publish_content$`Media App Media - Media → Gender`)
unique(publish_content$`Media App Media Category - Media Category → ID`)
unique(publish_content$`Media App Media Category - Media Category → Title`)
unique(publish_content$`Media App Media - Media → Is Celebrity`)
unique(publish_content$`Media App Media - Media → Is Influencer`)
unique(publish_content$`Media App Media - Media → Is Private`)



attr1 <- vector()
for (i in GoodPublisherIDs) {
  attr1 <- c( attr1, 
              (publish_content$`Media App Media Plan - Media Plan → Content Type`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr2 <- vector()
for (i in GoodPublisherIDs) {
  attr2 <- c( attr2, 
              (publish_content$`Media App Media Plan - Media Plan → Content Format`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr3 <- vector()
for (i in GoodPublisherIDs) {
  attr3 <- c( attr3, 
              (publish_content$`Media App Media Plan - Media Plan → Impression`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr4 <- vector()
for (i in GoodPublisherIDs) {
  attr4 <- c( attr4, 
              (publish_content$`Media App Media - Media → Is Private`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr5 <- vector()
for (i in GoodPublisherIDs) {
  attr5 <- c( attr5, 
              (publish_content$`Media App Media - Media → Audience Gender`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr6 <- vector()
for (i in GoodPublisherIDs) {
  attr6 <- c( attr6, 
              (publish_content$`Media App Media Category - Media Category → Title`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr7 <- vector()
for (i in GoodPublisherIDs) {
  attr7 <- c( attr7, 
              (publish_content$`Media App Media - Media → Is Influencer`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr8 <- vector()
for (i in GoodPublisherIDs) {
  attr8 <- c( attr8, 
              (publish_content$`Publisher Price`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}



attr9 <- vector()
for (i in GoodPublisherIDs) {
  attr9 <- c( attr9, 
              (publish_content$`Media Plan Price`)[which(publish_content$`Media App Media - Media → Publisher ID` == i)])
}




category <- publish_content$`Media App Media Category - Media Category → Title`
class(category)
category[1]



( uniqCatePub <- unique(category) )
#uniqCateAll <- na.omit(uniqCateAll)
#uniqCateAll
class(uniqCatePub)
length(uniqCatePub)
uniqCatePub[1]
uniqCatePub[40]
uniqCatePub[54]

#tempolar <- list()
#for (i in uniqCateAll) {
#  
#  tempolar[[i]] <- as.vector( which( cateAll == i ) )
#  
#}
#class(tempolar)
#tempolar[[1]]
#tempolar$آشپزی
#adver_camp$ID[tempolar$///////////]



names <- vector()
IDs <- vector()
n <- 0
for (i in c(1: length(uniqCateAll))) {
  k <- uniqCateAll[i]
  K <- as.vector( which( cateAll == k ) )
  for (j in K) {
    n <- n + 1
    jj <- adver_camp$`Advertiser ID`[j]
    names[n] <- k
    IDs[n] <- jj
  }
}

( adver_campIDsCategory <- data.frame( cbind( names, IDs)) )

#options("max.print" = 5000)

write_csv(x = adver_campIDsCategory , file =  "output/adver_campIDsCategory.csv")