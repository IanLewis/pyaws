import unittest
import sys

# quick-n-dirty for debug only
sys.path.append('..')
import ecs

class QueryTest( unittest.TestCase ):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testBadLicenseKey(self):
        ecs.setLicenseKey( "1MGVS72Y8JF7EC7JDZG0" )
        self.assertRaises( ecs.InvalidParameterValue, ecs.ItemLookup, "0596002818" )

    def testItemLookup(self):
        book = ecs.ItemLookup("0596009259")
        self.assertNotEqual( book, None)

        self.assertEqual( book.ASIN, u'0596009259' )
        self.assertEqual( book.Title, u'Programming Python' )
        self.assertEqual( book.Manufacturer, u"O'Reilly Media, Inc." )
        self.assertEqual( book.ProductGroup, u'Book' )
        self.assertEqual( book.Author, u'Mark Lutz')


    def testItemSearch(self):
        books = ecs.ItemSearch("python", SearchIndex="Books")
        self.assert_( len(books) > 9, "We are expect more than 9 books are returned." )

if __name__ == "__main__" :
    unittest.main()
