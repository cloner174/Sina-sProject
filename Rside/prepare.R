#
library(conflicted)
library(dplyr)
library(stringr)
#library(tidyr)
#library(tibble)




getwd()
#setwd("Rside/")





adver_camp <- read.csv("data/advertiser_campaigns.csv")
publish_content <- read.csv("data/publisher_contents.csv")





#View(publish_content)
#View(adver_camp)
class(publish_content)
class(adver_camp)

colnames(publish_content)
colnames(adver_camp)
dim(publish_content)
dim(adver_camp)





#Start with Smaller!

length(unique(adver_camp$ID))
length(unique(adver_camp$Advertiser.ID))
length(unique(adver_camp$Media.Plans.Filter...Categories))
length(unique(adver_camp$Campaign.Campaign.Category...Campaign.Category...ID))
length(unique(adver_camp$Publish.Period.Start))
length(unique(adver_camp$Campaign.Type))
length(unique(adver_camp$Manager.ID))
length(unique(adver_camp$Management.Percent.Fee))
length(unique(adver_camp$Quality.Of.Advertise))
length(unique(adver_camp$Quality.Of.Business))
length(unique(adver_camp$Is.Official))
length(unique(adver_camp$Is.Short.Link.Enabled))
length(unique(adver_camp$Is.Utm.Enabled))
length(unique(adver_camp$Is.Competition.Or.Has.Award))




dim(adver_camp)

advertiserDF <- adver_camp %>%
  select( c(ID,Advertiser.ID,Media.Plans.Filter...Categories,Campaign.Campaign.Category...Campaign.Category...ID,
            Campaign.Type, Manager.ID, Management.Percent.Fee, Is.Utm.Enabled,Publish.Period.Start,Budget,
            Quality.Of.Advertise, Quality.Of.Business,Is.Official, Is.Short.Link.Enabled,Is.Competition.Or.Has.Award) )



dim(advertiserDF)

unique(advertiserDF$Media.Plans.Filter...Categories)[2]
unique(advertiserDF$Media.Plans.Filter...Categories)[4]
##
( advertiserDF$Media.Plans.Filter...Categories[ which( advertiserDF$Media.Plans.Filter...Categories == 
                                                         unique(advertiserDF$Media.Plans.Filter...Categories)[2] )] <-
    NA )
##

##
( advertiserDF$Media.Plans.Filter...Categories[ which( advertiserDF$Media.Plans.Filter...Categories == 
                                                         unique(advertiserDF$Media.Plans.Filter...Categories)[4] )] <-
    NA )
##

advertiserDF <- na.omit(advertiserDF)

dim(advertiserDF)


uniqCateg <- unique(advertiserDF$Media.Plans.Filter...Categories)

uniqAdvers <- unique(advertiserDF$Advertiser.ID)

class(uniqCateg)
class(uniqAdvers)
length(uniqCateg)
length(uniqAdvers)


allcateg <- advertiserDF$Media.Plans.Filter...Categories
class(allcateg)
allcateg[1]
#strsplit(x = allcateg[1], split = "")



extractedCATEGORY2 <- vector()
for (eachCategory in uniqCateg) {
  
  temp <- str_extract_all(eachCategory, boundary("word"))

  for (j in temp) {
    
    for (p in j) {
      
      if ( isTRUE( p == "") == FALSE) {
        if (  isTRUE( p == "\"title_fa\"" ) == FALSE  ) {
          if (  isTRUE( p == "title_fa" ) == FALSE  ) {
            if (  isTRUE( p == "title" ) == FALSE  ) {
              if (  is.na( str_extract(p , "\\D+")) == FALSE  ) {
                print(p)
              }
            }
          }
        }
      }
    }
  }
  extractedCATEGORY2 <- c(extractedCATEGORY2, eachCategory)
}




extractedCATEGORY <- list()
for (i in c(1: length(uniqCateg))) {
  
  eachCategory <- uniqCateg[i]
  temp <- str_extract_all(eachCategory, boundary("word"))
  for (j in c(1: length(temp))) {
    temp2 <- temp[j]
    if ( j == 1) {
      extractedCATEGORY[[i]] <- c(extractedCATEGORY,  temp2 )
    }else{
      extractedCATEGORY[[i]][j] <- c(extractedCATEGORY[[i]], temp2 )
    }
  }
}



#for (j in c(1: length(eachCategory))) {
#$    
#$  }
#$  temp <- 
#  temp <- str_extract_all(eachCategory, boundary("word"))
#  
#  for (j in temp) {
#    
#    for (p in j) {
#      
#      if ( isTRUE( p == "") == FALSE) {
#        if (  isTRUE( p == "\"title_fa\"" ) == FALSE  ) {
#          if (  isTRUE( p == "title_fa" ) == FALSE  ) {
#v            if (  isTRUE( p == "title" ) == FALSE  ) {
#              if (  is.na( str_extract(p , "\\D+")) == FALSE  ) {
#                print(p)
#              }
#            }
#          }
#        }
#      }
#    }
#  }
#  extractedCATEGORY2 <- c(extractedCATEGORY2, eachCategory)
#}

extractedCATEGORY <- vector()
for (eachCategory in uniqCateg) {
  
  temp <- str_extract_all(eachCategory, boundary("word"))
  extractedCATEGORY <- c(extractedCATEGORY, temp)
}

extractedCATEGORYl2 <- vector()
for (templ2 in extractedCATEGORY) {
    if (condition) {
      
    }
    print(tempL2)
    break
    for (p in j) {
      
      if ( isTRUE( p == "") == FALSE) {
        if (  isTRUE( p == "\"title_fa\"" ) == FALSE  ) {
          if (  isTRUE( p == "title_fa" ) == FALSE  ) {
            if (  isTRUE( p == "title" ) == FALSE  ) {
              if (  is.na( str_extract(p , "\\D+")) == FALSE  ) {
                print(p)
              }
            }
          }
        }
      }
    }
  }
#  extractedCATEGORY2 <- c(extractedCATEGORY2, eachCategory)
  #}


( uniqCateAll <- unique(cateAll) )
uniqCateAll <- na.omit(uniqCateAll)
uniqCateAll
class(uniqCateAll)
length(uniqCateAll)
uniqCateAll[1]
uniqCateAll[40]
uniqCateAll[54]






tempolar <- list()
for (i in uniqCateAll) {
  tempolar[[i]] <- as.vector( which( cateAll == i ) )
}




advIDcamp <- list()
for (i in uniqCateAll) {
  for (j in c(1:length(tempolar[[i]]))) {
    tempTEmpo <- tempolar[[i]][j]
    if (j == 1) {
      advIDcamp[[i]] <- adver_camp$`Advertiser ID`[tempTEmpo]
    }else{
      advIDcamp[[i]] <- c( advIDcamp[[i]], adver_camp$`Advertiser ID`[tempTEmpo] )
    }
  }
}


class(tempolar)
tempolar[[1]]
class(advIDcamp)
advIDcamp[[1]]


#advIDcamp <- as.data.frame(advIDcamp)  Diff num of dim!


CateAdv <- vector()
AdvID <- vector()
for (i in uniqCateAll) {
  
  j <- i
  allIDs_temp <- as.vector( advIDcamp[[j]] )
  
  for (p in allIDs_temp) {
    
    CateAdv <- c(CateAdv, j)
    AdvID <- c(AdvID, p)
  }
}


( CateAdv_AdvID_DataFrame <- data.frame( cbind( CateAdv, AdvID)) )

#options("max.print" = 5000)

write_csv(x = CateAdv_AdvID_DataFrame , file =  "output/CateAdv_AdvID_DataFrame.csv")


attr1tempadv <- unique(adver_camp$`Quality Of Business`)

uniqAdvID_attr1



uniqAdvID <- unique(AdvID)
uniqAdvID_attr1 <- vector()
for (i in uniqAdvID) {
  j <- i
  tempuniqadvid <- which( adver_camp$`Advertiser ID` == j)
  uniqAdvID_attr1 <- c(uniqAdvID_attr1, ( adver_camp$`Quality Of Business`)[tempuniqadvid[1]] )
}
