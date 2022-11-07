# web_static

Learning about html and css and the goal of the tasks is to be able to fully understand
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSSWhat is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS


## TASKS

### 0. Inline styling

Write an HTML page that displays a header and a footer.

Layout:

* Body:
	* no margin
	* no padding
* Header:
	* color #FF0000 (red)
	* height: 70px
	* width: 100%
* Footer:
	* color #00FF00 (green)
	* height: 60px
	* width: 100%
	* text `Best School` center vertically and horizontally
	* always at the bottom at the page
Requirements:

* You must use the header and footer tags
* You are not allowed to import any files
* You are not allowed to use the style tag in the head tag
* Use inline styling for all your tags


**Files** - 1-index.html



### 1. Head styling

Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

* You must use the header and footer tags
* You are not allowed to import any files
* No inline styling
* You must use the style tag in the head tag
* The layout must be exactly the same as 0-index.html

**File** - 1-index.html


### 2. CSS files

Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

* You must use the header and footer tags
* No inline styling
* You must have 3 CSS files:
* styles/2-common.css: for global style (i.e. the body style)
* styles/2-header.css: for header style
* styles/2-footer.css: for footer style
* The layout must be exactly the same as 1-index.html


**Files**: 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css



### 4. Search!


Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

* Container:
	* between `header` and `footer` tags, add a `div`:
		* classname: `container`
		* max width 1000px
		* margin top and bottom 30px - it should be 30px under the bottom of the `heade`r (screenshot)
		* center horizontally
* Filter section:
	* tag `section`
	* classname `filters`
	* inside the `.container`
	* color white
	* height: 70px
	* width: 100% of the container
	* border 1px #DDDDDD with radius 4px
* Button search:
	* tag button
	* text Search
	* font size: 18px
	* inside the section filters
	* background color #FF5A5F
	* text color #FFFFFF
	* height: 48px
	* width: 20% of the section filters
	* no borders
	* border radius: 4px
	* center vertically and at 30px of the right border
	* change opacity to 90% when the mouse is on the button
Requirements:

* You must use: `header`, `footer`, `section`, `button` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
	* `styles/4-common.css:` for the global style (`body` and `.container` styles)
	* `styles/3-header.css:` for the header style
	* `styles/3-footer.css:` for the footer style
	* `styles/4-filters.css:` for the filters style
* `4-index.html` won’t be W3C valid, don’t worry, it’s temporary


**Files**: `4-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/4-filters.css`, `images/`



### 5. More filters

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

* Locations and Amenities filters:
	* tag: div
	* classname: locations for location tag and amenities for the other
	* inside the section filters (same level as the button Search)
	* height: 100% of the section filters
	* width: 25% of the section filters
	* border right #DDDDDD 1px only for the first left filter
	* contains a title:
		* tag: h3
		* font weight: 600
		* text States or Amenities
	* contains a subtitle:
		* tag: h4
		* font weight: 400
		* font size: 14px
		* text with fake contents

Requirements:

* You must use: header, footer, section, button, h3, h4 tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 4 CSS files:
	* styles/4-common.css: for the global style (body and .container styles)
	* styles/3-header.css: for the header style
	* styles/3-footer.css: for the footer style
	* styles/5-filters.css: for the filters style

**Files**: 5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/



### 6. It's (h)over

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
	* tag ul
	* classname popover
	* text should be fake now
	* inside each div
	* not displayed by default
	* color #FAFAFA
	* width same as the div filter
	* border #DDDDDD 1px with border radius 4px
	* no list display
	* Location filter has 2 levels of ul/li:
		* state -> cities
		* state name must be display in a h2 tag (font size 16px)
Requirements:

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 4 CSS files:
	* styles/4-common.css: for the global style (body and .container styles)
	* styles/3-header.css: for the header style
	* styles/3-footer.css: for the footer style
	* styles/6-filters.css: for the filters style

**Files**: 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/


### 7. Display results

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

* Add Places section:
	* tag: section
	* classname: places
	* same level as the filters section, inside .container
	* contains a title:
		* tag: h1
		* text: Places
		* align in the top left
		* font size: 30px
	* contains multiple “Places” as listing (horizontal or vertical) describe by:
		* tag: article
		* width: 390px
		* padding and margin 20px
		* border #FF5A5F 1px with radius 4px
		* contains the place name:
		* tag: h2
		* font size: 30px
		* center horizontally
Requirements:

* You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the img tag
* You are not allowed to use the style tag in the head tag
* All images must be stored in the images folder
* You must have 5 CSS files:
	* styles/4-common.css: for the global style (i.e. body and .container styles)
	* styles/3-header.css: for the header style
	* styles/3-footer.css: for footer style
	* styles/6-filters.css: for the filters style
	* styles/7-places.css: for the places style

**File**: 7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/