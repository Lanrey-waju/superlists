from selenium import webdriver
import unittest

class NewVisiorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lanre just learnt about this new to-do app. HE goes to check out its homepage
        self.browser.get('localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# He is invited to enter a to-do item straight away

# He types 'Pray Tahajjud' into a text box (Lanre likes to talk to His Creator)

# When he hits enter, the page updates, and now te page lists
#'1: 'Pray Tahajjud' as an item in a to-do list

# There is still a text bo inviting him to add another item.He enters 'Do some ironing' (Lanre likes to wear properly-ironed shirts to his day work) 

# The page updates again and he can now see both of his items on the list

# Lanre wonders whether the site will remember his list. Then he aees that the ssite has generaated a unique url for him

# He visits the url - his to-do list is still there

# Satisfied, he goes back to what he was doing prior
