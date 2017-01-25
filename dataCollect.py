#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import tweepy
import json
import time
import MySQLdb

#Variables that contains the user credentials to access Twitter API 
access_token = "766999276245221376-vBrbI2C7vCllPRb56O5sko2Ocn40uuJ"
access_token_secret = "weo8dbLeNA2ancEgJyMj258kw3r1zW3D9OX3SvUEXnrlB"
consumer_key = "tUbhzENsSXbdQ2dEmOP2fiOYz"
consumer_secret = "RYCYrdpmtNl3R6usXwlPcuMiQp8TXrgat4YPfZo3zyYWWDU1xn"




#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':  
    
    conn = MySQLdb.connect(host= "localhost",user="root",passwd="px2h-r7s",db="twitter_data")
    x = conn.cursor()
    trendlistNew=[]
    trendlist=["#10YearsOfOsnapitzari","#2Awesome","#3wordsbetterthanIloveyou","#4HSepang","#60daysinjail","#7YearsOfBaby","#80sSongsForCountries","#AcademyAwards","#ActiveJanoskians","#Advtravelconf","#AFCON2017","#AFCvBFC","#AfrobeatsWithAbrantee","#AJBellNBL","#All80sHour","#alternativefact","#alternativefacts","#andersonprog","#AppAwards16","#AppleTreeYard","#arcgap","#archantawards","#ARSBUR","#AskDanny","#AtlasV","#AusOpen","#AUSvPAK","#AwfullyBritishPubNames","#babyhour","#BadlyRecastAFilm","#BadRelationshipAdvice","#bbcaq","#bbcfootball","#bbcintroducing","#BBCIntroducingOnRadioWales","#bbcpm","#bbcqt","#bbcsp","#BBCTaboo","#BBNaija","#BeerBods","#BeingMaryJane","#Belfasthour","#beliebersstayforever","#Bellator170","#BernieEcclestone","#BestFans2017","#bettchat","#bhafc","#BigWeekend","#BizHour","#BlackAdam","#BloggerationChat","#bloggersbookfeast","#BOIMcKennaCup","#borolive","#botchedupbodies","#BOUWAT","#boycottadogspurpose","#Brexit","#bridgesnotwalls","#Brighton","#BritainsArmedHistory","#BritainsBenefitTenants","#C4PopUp","#CamilaBestFans","#careforthenhs","#Casualty","#CathyLive","#CBBNicola","#CBBStacey","#CBBUK","#CelebApprentice","#ChangeALetterRuinACelebrity","#charitytuesday","#CHEHUL","#ChewingGum","#ChewingGum2","#chocolatemovies","#clueless","#cmawards16","#ComicBookCharacterReportCards","#CommonSense","#ContainerMovies","#ConvinceMeToMarryYou","#CookSchoolGBC","#CopaDelRey","#cornwallhour","#courgettecrisis","#COYBIG","#COYR","#COYS","#CrappyBusinessProposals","#creativeshootout17","#CRYEVE","#CustomerServiceDosAndDonts","#DAPL","#DateMyFamily","#Davos","#ddduk","#deathinparadise","#DesertIslandDiscs","#Dispatches","#DisruptionSWT","#DIYstorebandsorsongs","#DolanTwinsNewVideo","#dorsethour","#Draghi","#DubaiMarathon","#eastenders","#ELEAGUEMajor","#Endeavour","#EnglandHour","#EngVsInd","#ENLScores","#ESRCRacisms","#EULCS","#EurovisionYouDecide","#FamousWhenYounger","#FashionRules","#FeministToDoList","#Fidelio","#FilmsForCricket","#firstdateshotel","#FirstDatesIRL","#flamablefamous","#FMQs","#FontSunday","#forgotten80s","#FridayFeeling","#Gambia","#GBvsATL","#GearsProCircuitMX","#GetYourTattsOut","#GFF17","#GGJ17","#GGJ2017","#GIDC","#giffgaffE4","#girlmeetsgoodbye","#globalgagrule","#GlobalWarning","#GLORY37","#GoDoEntAwards","#goglamgala","#GoodOmens","#Gotham","#Gpsbehindcloseddoors","#GrahamNorton","#HairdresserFilms","#HaloWC","#HandmadeHour","#Happy46thGary","#Hauk","#heavenclubspa","#hewillnotdivideus","#HFconference","#HighStakes","#HistoricalFigureASong","#HolbyCity","#Homeland","#homelesssunday","#Hoogerheide","#horizoncleaneating","#Hornchurch","#hospital","#hospitaltunage","#HSBC","#IAmLegend","#IamWhoIAmBecause","#ifgdirector","#IfYouCouldReadMyMind","#igot7selcaday","#ImagineNation","#IMarchWithLinda","#IMDOPodcast","#ImNotGoingToChurchBecause","#InauguralConcert","#InaugurateABandOrSong","#Inauguration","#InclusiveGrowth","#indiedevhour","#IndustrialStrategy","#INDvENG","#InsertNameHere","#InTech","#InTherapy","#IStandWithShane","#itsgoneviral","#ITVBoxing","#IWillAlwaysLove","#Jaws","#JuveLazio","#kavosink","#KillerCameron","#kitzbuehel","#LancashireHour","#LaughingMusic","#LetItShine","#LibraryAmbition","#Ligue1","#LinaresCrolla2","#Lionesses","#LittleMixBRITs","#Logan","#London","#LounielleIsOverParty","#LPWin","#LTC2017","#LTHEchat","#luxtravelchat","#makeasongasunday","#MakeSomebodyHeavier","#MakeSomeoneOlder","#MakeSomeoneSmelly","#Manchester","#MarkIsATool","#marr","#MCAwards16","#MCFCvTHFC","#MCITOT","#midlandshour","#midsomermurders","#MIDWHU","#MilanNapoli","#MK50","#mondaymotivation","#MostActiveCity","#MOTD","#MOTD2","#MotoGP","#MUNvR92","#Muskedragons","#MyCookingShowWouldBeAbout","#MyDayOffIn3Words","#MyFirstWordsAsPresident","#MyMumsHotterThanMe","#NathanielMGCup","#NationalCheeseLoversDay","#NationalHuggingDay","#Nationalpeanutbutterday","#NationalPieDay","#NationalPopcornDay","#NBAAllStar","#NewMusicFriday","#NFLPlayoffs","#NHCPerfume","#NinjaWarriorUK","#NoOffence","#NotGoingOut","#NudeActionMovies","#NZvBAN","#ODEONScreenUnseen","#OLOM","#OneFactAboutMe","#oneshow","#OscarNoms","#OurPerfectWedding","#PalermoInter","#PapaPennyAhee","#parliamentaryfilms","#Patriots","#penguinawarenessday","#Peston","#PhilosophersMovies","#pifdigital","#Plasco","#PLTonight","#PLYLIV","#PointlessCelebrities","#PrayForEllen","#presidentfart","#Pressconference","#productoftheyear","#producttank","#QPRFUL","#QSchool","#RaceofChampions","#ReasonsIAintInARelationship","#RenameMillionWomenMarch","#resist","#restorationman","#rhoa","#Ridge","#RLhfctor","#Rochdalehour","#ROCMiami","#RodentiaAMovieOrSong","#Rooney250","#RoyalBankBoost","#RSAeducation","#SanversIsBack","#saturdaynight","#SAvSL","#scotnight","#ScotSquad","#ScottishCup","#SeanSpicer","#SelfieForCindy","#selfieforseb","#SelfiesForAlly","#SeoulMusicAwards","#SGTNN2","#ShadowhuntersChat","#ShakespeareSunday","#sharedownership","#SickAnimals","#silvertowntunnel","#SLTchat","#SmearForSmear","#smellyfilms","#socialmobility","#somersethour","#SOULEI","#SoundOfMusicals","#SpicerFacts","#Sportscene","#SpyInTheWild","#SquirrelAppreciationDay","#StarsInCars","#stereounderground","#STKMUN","#StopYellowface","#suahour","#SundayBrunch","#SundayMorning","#sundayroast","#sunset","#Supergirl","#SuperSunday","#sussexhour","#T2trainspotting","#TelenetUCICXWC","#ThanksObama","#ThankYouObama","#TheAviators","#TheBigQuestions","#TheChrisRamseyShow","#TheHalcyon","#TheReassembler","#ThereIsNoEscapeFrom","#TheUndateables","#TheView","#TheVoice","#thevoiceuk","#ThingsINoLongerBelieve","#ThisMorning","#throughthekeyhole","#ThursdayThought","#TinaAndBobby","#tippingpoint","#toast","#TommyTiernanShow","#TOTP","#totp83","#TouchMusicVideo","#ToyFair2017","#Trainspotting","#TravelTuesday","#Trident","#Trump","#TrumpInauguration","#TuesdayMotivation","#TuringLecture","#TW3Awards","#twitterdisco","#ukbchour","#ukgcX","#Unforgotten","#UniversityChallenge","#upsetamovie","#USdebate","#USTitle","#VoteAllNight","#WalesWomen","#WBASUN","#WeAreWarriors","#WeAreWithAna","#WeCareAboutULiam","#WeCops","#weddinghour","#wednesdaywisdom","#wef17","#WEI2017","#Weird4WordInaugurationSpeech","#WGawards16","#WhyICantTalkToMyEx","#whyweloveashton","#WillAndGrace","#Willesden","#Winterwatch","#WithoutMyMorningCoffee","#WomensMarch","#womensmarchlondon","#WomenWhoHaveInspiredMe","#woofwoofwednesday","#WoolfWorks","#WordsByCamila","#worldwideawards","Aaron Rodgers","Adam Hadwin","Adama Barrow","Adama Traore","Aditya Chakrabortty","AFC Wimbledon","Aguero","Airdrie Savings Bank","Alderweireld","Alexander Arnold","Alibaba","Alistair Carmichael","All Stars","ALL WELCOME TO JOIN","Allan McGregor","Alonso","Amartya Sen","America","Amrezy","Andre Gray","Andre Marriner","Andreas Weimann","Andrew Crawford","Andrew Neil","Andy Carroll","Anfield","Angelina Jolie","Angelo Ogbonna","Angie","Anna Soubry","Anoeta","Anthony Taylor","Arcade Fire","Archer","Arrogate","Arron Banks","Arsenal","Article 50","Ashley Judd","Ashton Irwin","Astralis","Bacon","Bane","Barack Obama","Barbara Bush","Barkley","Barnsley","Basic Instinct","Bellerin","Ben Marshall","Ben Mee","Bernie Ecclestone","Bianca and Jamie","Big Show","BIGTHANKS","Bob Woodward","Bobby","Boris Johnson","Bournemouth 2-2 Watford","Bravo","Brexit","Bristol De Mai","British Cycling","Burnley","Cahill","Call of Cthulhu","Capital Force","Carlos Tevez","Carrick","Cech","Celta","Chapecoense","Charlie Adam","Chelsea","Chris Brunt","Chris Clements","Chris Martin","Chris Mears","Chris Wood","Chrissy Teigen","Christopher Samba","CIA HQ","Clattenburg","Clermont","Clichy","Climate Change Plan","Clyne","Coco Vandeweghe","Coleen","Coleman","COME ON ARSENAL","COME ON CHELSEA","Comical Ali","CONGRATS NIALL","Coquelin","Coutinho","Coutinho and Sturridge","CRIED","Crumlin Road","Daley","Dan Jarvis","Daniel May","Danny Murphy","Danny Rose","Darlow","Darren Fletcher","Dave Jones","David Davis","David Meyler","De Bruyne","De Gea","Deadpool","Deepdale","Dele Alli","Dembele","Depay","Dhoni","Dier","Doherty","Donald Trump","Doukara","Draghi","Dybala","Ed Miliband","Eddie Jones","Eden Gardens","Edwards","EGOT","El Chapo","Emmanuel Adebayor","Emre Can","England by 15","Escape to Victory","Etihad","Ewan McGregor","Fabianski","Fabregas","Falcons","Father John Misty","Fikayo Tomori","Fire Emblem","Firmino","First Lady","Flaming Lips","Fonte","Fox News","Foxes","Frank Turner","French Socialist","Friends with Benefits","FULL TIME","Funes Mori","Future Islands","Gabriel Jesus","Garbine","Genie","George Osborne","George Soros","Ghoulam","Gillian Troughton","Glasgow Airport","Goldberg","Goldman Sachs","Gorden Kaye","Gorillaz","Granit Xhaka","Gray","Green Bay","Guinea-Bissau","Gunners","Hacksaw Ridge","HALF TIME","Hallelujah Money","Handsworth","Harry Maguire","Harry Wilson","Harry Winks","Haydock","Hearts","Heidi and Spencer","Hennessey","Henri Lansbury","Henrik Stenson","Hercules","Highs of 5C","Hillary","Hornchurch","Howard Webb","Hugo","Hugo Lloris","I Am Legend","Iago Aspas","Ian Paisley","Ibra","Ighalo","Industrial Strategy","Iwobi","Jadhav","Jake Ball","Jake Cooper","Jake Humphrey","Jake Livermore","Jaki Liebezeit","James Ward-Prowse","Jamie Vardy","Jason Roy","Jaws","Jay Rodriguez","Jermaine Pennant","Jezki","Jodie Marsh","Joe Perry","Joel Matip","Joey Barton","Jon Moss","Jon Voight","Jonjo Shelvey","Jordan Ayew","Jose Fonte","Kante","Kashmir","Kasim","Keir Starmer","Kellyanne Conway","Kenny Miller","Kerim Frei","Kevin Friend","Kevin Owens","Kevin Stewart","Keystone XL and Dakota Access","KICK OFF","Kim Woodburn","Kingsholm","Kitzbuhel","KLAROLINE STOLE OUR HEARTS","Kohli","Koscielny","Kosovo","Labour MPs","Lallana","Lamela","Lansbury","Law Abiding Citizen","Lazar Markovic","Lee Grant","Leighton Baines","Leonardo Ulloa","Leopardstown","Lescott","Lewisham","Liberty Media","Lincoln City","Lingard","Liz Carr","Llorente","Lloris","London","Looper","Lord Byron","Lorient","Lucas","Lucas Leiva","Luis Hernandez","Luis Suarez","Luke McCormick","Madonna","Maggie","Makarova","Man City 2-2 Tottenham","Mannone","Marco Fu","Marco van Basten","Marcus Haber","Marney","Marriner","Martin McGuinness","Martin Schulz","Mason Mount","Mata","Match of the Day","Mathlouthi","Matt Ritchie","Matty Ice","Meitu","Mel Gibson","Melania","Memphis","Men's March","Meydan","Michael Fallon","Michael Flatley","Michelle O'Neill","Michelle Obama","Mick","Micro Machines","Middlesbrough 1-2 West Ham","Middlesbrough 1-3 West Ham","Mignolet","Miguel Ferrer","Mikael Lustig","Mike Dean","Milner","Mischa Zverev","Mkhitaryan","Moreno","MOTD","Motherwell","Mr Big Shot","Munster v Toulouse","Murphy","Murray","Napoli","Nathan Holland","Nazanin Zaghari-Ratcliffe","Nazis","Neil Oliver","Neon Wolf","New Gen","Newcastle 2-0 Birmingham","Newcastle 3-1 Birmingham","Niall Keown","Niall Quinn","Nicola","Nicola Sturgeon","Nicole Cooke","Nocturnal Animals","Novak Djokovic","Number 7","NYFW","Oakwell","Okazaki","Olivier Giroud","Olsson","Origi","Osasuna","Otamendi","Owen Smith","Packers","Panenka","Papua New Guinea","Paris Jackson","Park Lane","Pascal Lamy","Patrick Bamford","Patrick Roberts","Patrick Stewart","Paul Hunter","Paul Nuttall","Paulo Alves","PENALTY SOUTHAMPTON","PENALTY TO LIVERPOOL","Per Mertesacker","Perry","Peter Mandelson","Piers Morgan","Plane","Plymouth","Poch","Police Taser","Poppy Widdison","Power Rangers","Press Secretary","Prince Harry","Progress 8","PSNI","Race Relations Advisor","Rachael Heyhoe Flint","Rafa Nadal","Raith","Ramsey","Ranieri","Rashford","Reagan","Really Special","RED CARD","Redmen","Reigns","Richard Spencer","Riverdance","Rob Green","Robbie","Robbie Davies","Robbie Savage","Robert Hannigan","Rod Stewart","Roger Federer","Ronald Koeman","Ronnie O'Sullivan","Ross Brawn","Ross McCormack","Rumble","Rusev","Ryan Christie","Ryan Kent","Ryan Mason","Sadio Mane","Saido Berahino","Sam Morsy","Sam Warburton","Sami","Samoa","San Antonio","Sanchez","Sane","Santas","Scarlett Johansson","Schladming","Schlupp","Schmeichel","School of Rock","Scott Sinclair","Sean Dyche","Sean Spicer","Selhurst Park","Senegal","Serena","Serena Williams","Sergio Ramos","Seth","Seth Rollins","Seumas Milne","Shane Long","Sharif","Shayla","Shearer","Shelvey","Sheyi Ojo","Shia LaBeouf","Silva","Sincil Bank","Sir Bobby Charlton","Sir Patrick Coghlin","Sizing John","Slaven Bilic","Smalling","Sniper Elite 4","Southwell","Spencer","Spurs","Status Quo","Steelers","Stefan","Sterling","Steve Bruce","Steve Mcmanaman","Steven Gerrard","Still 0-0","Stoke","Stoke and Copeland","Str8 Grove","Strycova","Stuani","Stuart Findlay","Suicide Squad","Super Bowl","Super Sunday","Supreme Court","Supreme x Louis Vuitton","Surrey County Council","Sveta","Swansea","Sweet Charity","T2 Trainspotting","Taser","Tasered","TEAM NEWS","Tel Aviv to Jerusalem","Terminator","Thames","The Cadbury's Premier League","The Day After Tomorrow","The Foreign Office","The Last Jedi","The Mirror","The Other Woman","The Piano Guys","The Ring","The Storyteller","The Variety Bazaar","Time Bandits","Tiote","Toby Keith","Tom Arscott","Tom Baker","Tom Brady","Tom Carroll","Tom Daley","Tom Tyrrell","Tommy Fleetwood","Top 4","Trans-Pacific Partnership","Trident","Trinity Mirror","Triple H","Trump","Tsonga","Uganda","Valdes","Van Basten","Van Dijk","Vardy","Venus Williams","Victor Moses","Villa Park","Walker","Wanyama","Washington","Washington DC","Wasps","Wayne Rooney","Weather","Weekend League","Welbeck","Welford Road","Wenger","Wes Burns","Wes Morgan","West Bank","Westbrook","White House","Wijnaldum","Wimmer","Woakes","Woody Johnson","Xhaka","Yakuza 0","Yorkhill","Yorkshire Bank","Yuvraj","Zabaleta","Zebre","Zverev"]
    print(len(trendlist))
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=False)
    
    while 1 :
    	trends1 = api.trends_place(id=44418)
    	data = trends1[0]

    	trends = data['trends']
    	hashtags=0
	urls=0
	retweeted=0
    	names = [trend['name'] for trend in trends]
    	trendlistNew=[trend for trend in names if trend not in trendlist]
	print trendlistNew
    	for topic in trendlistNew:
		try:
			first=True
    			#new_tweets=json.dumps(new_tweets) 
    			for tweet in  tweepy.Cursor(api.search,q=topic,rpp=400,result_type="recent",include_entities=True).items(400):
				#if tweet["lang"]=='en' or tweet["lang"]=='gr' :
				try:    
					userId= tweet.user.id
					tweetId=tweet.id
					text = tweet.text.encode('utf-8')
					text = text.replace('\n', ' ').replace('\r',' ')
					text = text.replace('\t', ' ').replace('\r',' ')
					text = text.replace('"', ' ').replace('\r',' ')
					for hashtag in tweet.entities["hashtags"]:
						hashtags += 1
					for link in tweet.entities["urls"] :
						urls +=1
					try:	
						tweet.retweeted_status
					except AttributeError:
						retweeted=0
					else :
						retweeted=1
					lang = tweet.lang
					timestamp = tweet.created_at
					timestamp=str(timestamp).split(' ')
					#print str(tweetId)+"\t"+str(userId)+"\t"+str(text)+"\t"+str(hashtags)+"\t"+str(urls)+"\t"+str(retweeted)+"\t"+str(lang)+"\t"+str(tweet.retweet_count)+"\t"+str(tweet.favorite_count)+"\t"+str(timestamp[0])+"\t"+str(timestamp[1])+"\t"+str(topic)					
					if first :
						first=False
						try:
							x.execute("INSERT INTO `topics` (`name`) VALUES (\""+str(topic)+"\")")
							conn.commit()	
							print "succees on topic"
						except:
							print "error on topic"
							print conn.rollback()
					try:
						x.execute("INSERT INTO `tweets` (`id`, `tweet_id`, `user_id`, `tweet_text`, `hashtags_count`, `url_count`, `is_retweeted`, `lang`, `retweet_count`, `favorite_count`, `date`, `time`, `topic`) VALUES (NULL,\""+str(tweetId)+"\",\""+str(userId)+"\",\""+str(text)+"\",\""+str(hashtags)+"\",\""+str(urls)+"\",\""+str(retweeted)+"\",\""+str(lang)+"\",\""+str(tweet.retweet_count)+"\",\""+str(tweet.favorite_count)+"\",\""+str(timestamp[0])+"\",\""+str(timestamp[1])+"\",\""+str(topic)+"\")")
						conn.commit()	
						print "succees on tweet"
					except:
						print "error on tweet"
						print conn.rollback()
					hashtags=0
					urls=0
					retweeted=0
				except ValueError:
					print "error"
					continue
		except ValueError:
			continue
				
	trendlist += trendlistNew 
	trendlistNew=[]
	time.sleep(60*15)
