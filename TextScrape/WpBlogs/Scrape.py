
import logSetup
if __name__ == "__main__":
	print("Initializing logging")
	logSetup.initLogging()

import TextScrape.WordpressScrape

import webFunctions


class Scrape(TextScrape.WordpressScrape.WordpressScrape):
	tableKey = 'wp'
	loggerPath = 'Main.Wp.Scrape'
	pluginName = 'WpScrape'

	wg = webFunctions.WebGetRobust(logPath=loggerPath+".Web")

	IGNORE_MALFORMED_URLS = True
	threads = 6

	baseUrl = [
		'http://9ethtranslations.wordpress.com',
		'http://amaburithetranslation.wordpress.com',
		'http://fateapocryphathetranslation.wordpress.com',
		'http://fuyuugakuenthetranslation.wordpress.com',
		'http://gjbuthetranslation.wordpress.com',
		'http://grimgalthetranslation.wordpress.com',
		'http://hellotranslations.wordpress.com',
		'http://hennekothetranslation.wordpress.com',
		'http://kobatochandaisuki.wordpress.com',
		'http://korezombiethetranslation.wordpress.com',
		'http://loveyouthetranslation.wordpress.com',
		'http://maoyuuthetranslation.wordpress.com/',
		'http://mayochikithetranslation.wordpress.com',
		'http://ojamajothetranslation.wordpress.com',
		'http://oregairuthetranslation.wordpress.com',
		'http://oreimothetranslation.wordpress.com',
		'http://rokkathetranslation.wordpress.com/',
		'http://sasamisanthetranslation.wordpress.com',
		'http://seizonthetranslation.wordpress.com',
		'http://skyworldthetranslation.wordpress.com',
		'http://solitarytranslation.wordpress.com/',
		'http://thecatscans.wordpress.com/',
		'http://tsaltranslation.wordpress.com',
		'http://zmunjali.wordpress.com',
		'https://xantbos.wordpress.com/',
		'https://9ethtranslations.wordpress.com/',
		'https://binhjamin.wordpress.com',
		'https://bluesilvertranslations.wordpress.com',
		'https://defiring.wordpress.com/',
		'https://hokagetranslations.wordpress.com',
		'https://kyakka.wordpress.com',
		'https://kyakka.wordpress.com/',
		'https://lorcromwell.wordpress.com/',
		'https://mahoutsuki.wordpress.com/',
		'https://manga0205.wordpress.com/',
		'https://metalhaguremt.wordpress.com',
		'https://nanodesutranslations.wordpress.com/',
		'https://oniichanyamete.wordpress.com/',
		'https://pirateyoshi.wordpress.com/',
		'https://sakurahonyaku.wordpress.com/',
		'https://setsuna86blog.wordpress.com/',
		'https://tomorolls.wordpress.com',
		'https://tsuigeki.wordpress.com/',
		'https://unbreakablemachinedoll.wordpress.com/',
		'https://wartdf.wordpress.com/',
		'https://yoraikun.wordpress.com/',
		'https://zmunjali.wordpress.com/',
		'https://setsuna86blog.wordpress.com/',
		'https://tensaitranslations.wordpress.com/',
		'https://gekkahimethetranslation.wordpress.com/',
		'https://ohanashimi.wordpress.com/',

		'http://gravitytranslations.wordpress.com/',
		'http://gravitytranslations.com/',             # The wordpress address redirects to the plain URL
	]

	startUrl = 'https://binhjamin.wordpress.com'

	# Any url containing any of the words in the `badwords` list will be ignored.
	badwords = [
				"/manga/",
				"/recruitment/",
				"wpmp_switcher=mobile",
				"account/begin_password_reset",
				"/comment-page-",

				# Why do people think they need a fucking comment system?
				'/?replytocom=',
				'#comments',
				"_wpnonce=",
				'public-api.wordpress.com'
				# Mask out the PDFs
				"-online-pdf-viewer/",

				# Who the fuck shares shit like this anyways?
				"?share=",

				]

	decompose = [


		{'class'           : 'authorpost'},
		{'class'           : 'bit'},
		{'class'           : 'blog-feeds'},
		{'class'           : 'blog-pager'},
		{'class'           : 'btop'},
		{'class'           : 'column-left-outer'},
		{'class'           : 'column-right-outer'},
		{'class'           : 'commentlist'},
		{'class'           : 'comments'},
		{'class'           : 'comments-link'},
		{'class'           : 'date-header'},
		{'class'           : 'entry-meta'},
		{'class'           : 'entry-utility'},
		{'class'           : 'footer'},
		{'class'           : 'footer-outer'},
		{'class'           : 'header-outer'},
		{'class'           : 'headerbg'},
		{'class'           : 'komensamping'},
		{'class'           : 'loggedout-follow-normal'},
		{'class'           : 'menujohanes'},
		{'class'           : 'nav-menu'},
		{'class'           : 'navbar'},
		{'class'           : 'photo-meta'},
		{'class'           : 'post-feeds'},
		{'class'           : 'post-footer'},
		{'class'           : 'quickedit'},
		{'class'           : 'sd-content'},
		{'class'           : 'sd-title'},
		{'class'           : 'sidebar'},
		{'class'           : 'tabs-outer'},
		{'class'           : 'widget-area'},
		{'class'           : 'widget-container'},
		{'class'           : 'widget-content'},
		{'class'           : 'wpa'},   # Ads, I think.
		{'class'           : 'wpcnt'},
		{'class'           : 'wpcom-follow-bubbles'},
		{'class'           : 'xoxo'},
		{'id'              : 'access'},
		{'id'              : 'bit'},
		{'id'              : 'branding'},
		{'id'              : 'calendar_wrap'},
		{'id'              : 'carousel-reblog-box'},
		{'id'              : 'colophon'},
		{'id'              : 'comments'},
		{'id'              : 'credit-wrapper'},
		{'id'              : 'entry-author-info'},
		{'id'              : 'footer'},
		{'id'              : 'header'},
		{'id'              : 'header-meta'},
		{'id'              : 'headerimg'},
		{'id'              : 'infinite-footer'},
		{'id'              : 'jp-post-flair'},
		{'id'              : 'likes-other-gravatars'},
		{'id'              : 'nav-above'},
		{'id'              : 'nav-below'},
		{'id'              : 'respond'},
		{'id'              : 'secondary'},
		{'id'              : 'sidebar'},
		{'id'              : 'sidebar-wrapper'},
		{'id'              : 'sidebar-wrapper1'}, # Yes, two `sidebar-wrapper` ids. Gah.
		{'id'              : 'site-header'},
		{'id'              : 'site-navigation'},
		{'name'            : 'likes-master'},
		{'style'           : 'display:none'},



	]

	decomposeBefore = [


		{'name'  : 'likes-master'},  # Bullshit sharing widgets
		{'class' : 'comments'},
		{'class' : 'comments-area'},
		{'class' : 'wpcnt'},
		{'id'    : 'addthis-share'},
		{'id'    : 'comments'},
		{'id'    : 'info-bt'},
		{'id'    : 'jp-post-flair'},

	]

	stripTitle = [
		"| KobatoChanDaiSukiScan",
		"| Hokage Translations",
		"| 1HP",
		"| Blue Silver Translations",
		"| Krytyk's translations",
		"| Light Novel translations",
		"| LorCromwell",
		"| mahoutsuki translation",
		"| Novel Translation",
		"| TheLazy9",
		"| Tomorolls",
		"| Ziru's Musings",
		'| Gravity translation',
		'| HaruPARTY Translation Group',
		'| Kyakka',
		'| manga0205',
		'| SETSUNA86BLOG',
		'| Solitary Translation',
		'| Sousetsuka',
		'| Tsuigeki Translations',
		'| Unbreakable Machine Doll',
		'| Unlimited Novel Failures',
		'| なのですよ！',
		'| 桜翻訳!',
		'(NanoDesu)',
		'A Translation of the',
		'Roxism HQ |',
		'| SETSUNA86BLOG',
		'mahoutsuki translation |'
	]


	# def checkDomain(self, url):
	# 	return False

	def postprocessBody(self, soup):
		for style_tag in soup.find_all('style'):
			style_tag.decompose()
		for mid_span in soup.find_all("span", _class="c3"):
			mid_span.unwrap()
		return soup

def test():
	scrp = Scrape()
	scrp.crawl()
	# scrp.retreiveItemFromUrl(scrp.startUrl)


if __name__ == "__main__":
	test()




