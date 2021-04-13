import re

text_to_search = '''
abcdefijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

india.com

321-555-4321
123.555.1234
800.555.1245
900-555-5452

Mr. Singh
Mr Sharma
Ms David
Mrs. Robinson
Mr. G

cat
mat
bat
pat
'''

sentence = 'Start a sequence and then bring it to an end'
# compile method will allow us to seperate all our pattern into a variable & also use it for multiple searches
# pattern = re.compile(r'^Start')


'''to search phone number we need to use Metacharacters instead of literal character
and create a pattern as it consists of 3 digits - and dots(period)'''
# dot(.) prints any character and period
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]d\d\d\d')


# pattern = re.compile(r'[1-5]')     #prints 1 to 5 as range
# pattern = re.compile(r'[a-z')      #print a to z
# pattern = re.compile(r'[a-zA-Z')   #upper and lower case letter both
# pattern = re.compile(r'^a-zA-Z')   #print not lower & upper case, we get newline etc
# pattern = re.compile(r'[^b]at')    #print not starting with b, it negates

'''
Quantifiers:
*   - 0 or More
+   - 1 or more
?   - 0 or more
{3} - exact numbers
{3.4}   - range of numbers (min, max)
'''
# search using quantifiers - (3} takes 3 digit range
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# pattern = re.compile(r'Mr\.?')  # ? makes the period optional

# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')    #* print 0 or more char

# how to check Mr and Ms together
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # print complete name together


emails = '''
pk.airsqn@gmail.com
india@in.com
11.pk.29@in.com
alpha-321-mike@gmail.com
'''
# # pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|in)')
#
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*')
# #match the search in text_to_search
# matches = pattern.finditer(emails)

# MAtch urls
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w*)')

# pattern = re.compile(r'end', re.I)
# match the search in text_to_search
matches = pattern.search(urls)
# print(matches)
# to print the matches
for match in matches:
    print(match)
    # print(match.group(3))    #group will print the groups such as www | domain name etc

#
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]d\d\d\d')
# #to check phone no from a file
# with open('sample.csv', 'r', encoding='utf-8') as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#
#     for match in matches:
#         print(match)
print(pattern)
