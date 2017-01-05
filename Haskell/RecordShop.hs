-- |This program simulates a record shop.

type Name = String
type Phone = String
type Address = [String]
type SongTitle = String
type Artist = String
type Duration = Int
type ReviewScore = Int
type CustomerID = Int
type ReviewBody = String
type CardNumber = String
type CardHolder = String



data Customer = Customer {
	  name    :: Name ,
	  phone   :: Phone ,
	  address :: Address
	 } deriving (Show)

data BillingInfo = CreditCard {
	 number   :: CardNumber ,
	 customer :: Customer
	 } deriving (Show)	

data SongInfo = Song {
	songName  :: SongTitle ,
	artist    :: Artist ,
	time      :: Duration 
	} deriving (Show)

data SongReview = Review {
	song     :: SongInfo ,
	reviewer :: Customer ,
	score    :: ReviewScore ,
	review   :: ReviewBody
	} deriving (Show)


customer1 = Customer "Dylan Grande" "2033395760" ["Fairfield", "CT"]
billing1 = CreditCard "290888585945049" customer1
song1 = Song "Grande Season" "Dylon Dylon" 345
review1 = Review song1 customer1 5 "Dope Song!!"


main = do
	print customer1 
	putStr "\nCustomer Billing Info\n"
	print billing1 
	putStr "\nCustomer Review\n" 
	print review1
	

	   

