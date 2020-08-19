import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "https://www.google.com/search?q=ckexfqyjt+xbckj&oq=ckexfqyjt+&aqs=chrome.1.69i57j69i59.2782j0j4&sourceid=chrome&ie=UTF-8"
login_page = browser.get(url)
tag = login_page.soup.select("#Zv1Nfb")
print(tag.text)
# login_html = login_page.soup
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "arester1980"
# form.select("input")[1]["value"] = "lenosh80"
# profiles_page = browser.submit(form, login_page.url)
# print(profiles_page.url)