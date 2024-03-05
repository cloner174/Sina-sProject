
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

#categori <- adver_camp$`Media Plans Filter → Categories`
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
    n <- n + 1
    jj <- adver_camp$ID[j]
    names[n] <- k
    IDs[n] <- jj
  }
}

( adver_campIDsCategory <- data.frame( cbind( names, IDs)) )

#options("max.print" = 5000)

write_csv(x = adver_campIDsCategory , file =  "output/adver_campIDsCategory.csv")


