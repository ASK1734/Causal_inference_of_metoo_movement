harrass = read.csv("/Users/chenshaokai/Desktop/工作/中研院/me_too/Alan/google trend & victim list/rawdata/panel_data.csv")

harrass$id <- as.numeric(as.factor(harrass$id))
# harrass$t <- as.numeric(as.factor(harrass$t))

harrass <- na.omit(harrass)

harrass <- subset(harrass, select = -X)

within_reg <- plm(Sit ~ Tit + Ait + sumAit + lagRi + lagRj + t, 
                   data = harrass, 
                   #family = binomial("logit"), # in plm adding this doesn't work or change any thing, this is for pglm
                   index = c("id"), 
                   model = "within",
                   effect = "individual",) 
                   #start = as.vector(init_coeffs))

summary(within_reg)

#harrass$industry <- as.factor(harrass$industry)
harrass$industry <- relevel(harrass$industry, ref = "Other")
dummy_reg = glm(Sit ~ Tit + Ait + sumAit + lagRi + lagRj + factor(industry) + factor(id) + factor(t), data = harrass)
options(max.print=10000)
summary(dummy_reg)

glm_reg = glm(Sit ~ Tit + Ait + sumAit + lagRi + lagRj +  factor(industry), data = harrass)
summary(glm_reg)
