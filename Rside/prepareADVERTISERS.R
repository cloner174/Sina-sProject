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


uniqAdvers <- unique(advertiserDF$Advertiser.ID)

class(uniqAdvers)
length(uniqAdvers)
allcateg <- advertiserDF$Media.Plans.Filter...Categories
class(allcateg)
allcateg[1]


#strsplit(x = allcateg[1], split = "")
num_ = 1
for (eachCategory in allcateg) {
  
  temp <- str_extract_all(eachCategory, boundary("word"))
  
  for (j in temp) {
    
    for (p in j) {
      
      if ( isTRUE( p == "") == FALSE) {
        if (  isTRUE( p == "\"title_fa\"" ) == FALSE  ) {
          if (  isTRUE( p == "title_fa" ) == FALSE  ) {
            if (  isTRUE( p == "title" ) == FALSE  ) {
              
              if (  is.na( str_extract(p , "\\D+")) == FALSE  ) {
                
                advertiserDF$Media.Plans.Filter...Categories[[num_]] <- p
                break
                }
            }
          }
        }
      }
    }
    num_ = num_+1
  }
}
allcateg <- advertiserDF$Media.Plans.Filter...Categories
allcateg[1]
allcateg[20]
allcateg[200]



library(polyglotr)

num__ = 1
for ( i in advertiserDF$Media.Plans.Filter...Categories) {
  advertiserDF$Media.Plans.Filter...Categories[num__] <- 
    polyglotr::google_translate(i, target_language = "en", source_language = "fa")
  num__ = num__+1
}
#options("max.print" = 5000)

write.csv(x = advertiserDF , file =  "output/advertisers.csv")

#end1