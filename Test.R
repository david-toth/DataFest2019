require(stats)



#plot(SleepHours, AccelImpulse)
#lines(lowess(AccelImpulse))

#plot(SleepHours)

#plot(table(rpois(100, 5)), type = "h", col = "red", lwd = 10,
#     main = "rpois(100, lambda = 5)")
nData = 16

Average_Sleep = rep(0,nData)
Average_Impulse = rep(0,nData)
Average_Speed = rep(0,nData)
#fatigueavg = rep(0,nData)
Average_Desire = rep(0,nData)
Average_Acceleration = rep(0,nData)

for (i in 1:nData){
  Average_Sleep[i] = mean(wellness$SleepQuality[wellness$PlayerID==i]);
  Average_Acceleration[i] = mean(gps$AccelLoad[gps$PlayerID==i]);
  Average_Speed[i] = mean(gps$Speed[gps$PlayerID==i]);
 # fatigueavg[i] = mean(wellness$Fatigue[wellness$PlayerID==i]);
  Average_Desire[i] = mean(wellness$Desire[wellness$PlayerID==i]);
  Average_Impulse[i] = mean(wellness$Desire[wellness$PlayerID==i]);
}



sleepimpulse = cov(cbind(Average_Sleep, Average_Impulse, Average_Speed, Average_Desire, Average_Acceleration))

sleepimpulscore= cov2cor(sleepimpulse)

library(corrplot)
corrplot(sleepimpulscore, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45) + theme(rect = element_rect(fill = "transparent"))
# Insignificant correlation are crossed
#corrplot(res2$r, type="upper", order="hclust", 
        # p.mat = res2$P, sig.level = 0.01, insig = "blank");
# Insignificant correlations are leaved blank
#corrplot(res2$r, type="upper", order="hclust", 
        # p.mat = res2$P, sig.level = 0.01, insig = "blank");

#Step1: corr to calculate correlation matrix

#points(x, cex = .5, col = "dark red")

#average acceleration impulse over the day, to match with sleep hours (temoral resoluition) 
