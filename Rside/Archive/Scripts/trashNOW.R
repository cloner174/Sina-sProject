
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


#attr1tempadv <- unique(adver_camp$`Quality Of Business`)

#uniqAdvID_attr1








uniqPublisherCateg <- unique(PublisherDataFrame$Media.App.Media.Category...Media.Category...Title)

class(uniqPublisherCateg)
length(uniqPublisherCateg)
head(uniqPublisherCateg)

uniqPublisherCategTranslate <- vector()

for (i in uniqPublisherCateg) {
  uniqPublisherCategTranslate <- c(uniqPublisherCategTranslate, polyglotr::google_translate(i, target_language = "fa", source_language = "en"))
}

length(uniqPublisherCategTranslate)
head(uniqPublisherCategTranslate)


allcateg <-   PublisherDataFrame$Media.App.Media.Category...Media.Category...Title

PublisherDataFramecopy()

for (i in PublisherDataFrame$Media.App.Media.Category...Media.Category...Title) {
  PublisherDataFrame$Media.App.Media.Category...Media.Category...Title <- polyglotr::google_translate(i, target_language = "fa", source_language = "en")
}

class(allcateg)



uniqAdvID <- unique(AdvID)
uniqAdvID_attr1 <- vector()
for (i in uniqAdvID) {
  j <- i
  tempuniqadvid <- which( adver_camp$`Advertiser ID` == j)
  uniqAdvID_attr1 <- c(uniqAdvID_attr1, ( adver_camp$`Quality Of Business`)[tempuniqadvid[1]] )
}
