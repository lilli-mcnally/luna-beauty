# Luna Beauty
*A makeup ecommerce website where users can browse, filter and sort products. Features a working Checkout app and the ability to create and update a user profile.*

![Am I Responsive](./static/README/am-i-responsive.PNG)

## Purpose and Value

### User Stories
> A young person is looking for a glittery eye shadow for a party they're going to.

> A person in their mid-fifties want a new foundation that suits their skin tone well. 

### User Goals
Users want to be able to browse the website for different make up. They want to be able to filter by type, rather than scrolling through every item on the website.

They'd also like shipping costs added to their total, and any discounts automatically adjusted in their shopping bag.

### Website Goals
To provide users with an easy to use website for browsing make up. To have an attractive home page that showcases a range of products.

### Competitor Reviews

#### Beauty Bay
Pros
> The home page grabs the users attention with large bold images. The Navigation bar is well set out underneath a search bar, that has icons to log in, see your wishlist, and your bag.

Cons
> Once users click the Nav bar items, a huge dropdown appears with a lot of options, which makes it more difficult to navigate to exactly what you need as the content is overwhelming.

#### Boots
Pros
> Once looking through products, the page is clean and easy to read. Users can add a product straight to their basket. Products that come in a range of colours take you to the product page to select the colour you like before adding to basket.

Cons
> The navigation has a lot of different product types, so users looking for Mascara for example, need to search through three Navigation selections, and then filter for Mascara. On the product page, the information isn't collapsible so there's a lot of information constantly on display.

## Objectives

| Objective           | Importance | Viability / Feasibility | To be added |
|------------|------------|-------------------------|--------|
| Users can browse several products using card to display images and brief information |  4  |   5   |  :heavy_check_mark:  |
| Users can choose a colour of a product and add it to their basket  |   5    |   5   | :heavy_check_mark: |
| Users can leave and read reviews for products   |  3  |  2   |    |
| Users are able to save their name and address to their account when checking out |  3  |  4  | :heavy_check_mark: |
| Users can see their order on their profile or in their confirmation email |   4   |   4  | :heavy_check_mark:     |

##### Future features
* Add the option to review items
* Expand the range to include skincare
* Add blog pages about recommendations for products.
* Add the option to log in using Facebook or Google
* Add a Wishlist option to the profile

## Wireframes
* [Home Page](./static/README/home.PNG)
* [Products Page](./static/README/products.PNG)
* [Product Details Page](./static/README/product-info.PNG)
* [Bag page](./static/README/basket.PNG)
* [Checkout Page](./static/README/payment.PNG)
* [Checkout Success Page](./static/README/order-successful.PNG)
* [Profile Page](./static/README/profile.PNG)
* [Login Page](./static/README/login.PNG)
* [Sign Up Page](./static/README/sign-up.PNG)

## Prototype
* [Prototype Home Page](./static/README/prototype.PNG)



## Fixed Bugs

#### Delivery Cost
I tried adding my delivery costs to my total costs once the discount had been removed (if necessary) in the bag app. However, I had an error showing that said I couldn’t add a decimal and a float. I researched on Google and found a really interesting website called [Tiny Struggles](https://tinystruggles.com/posts/django_decimals/) which helped me convert my float into a decimal by using:

`from decimal import Decimal`

and then amending my discount using:

`discount = Decimal((total / 100) * settings.DISCOUNT_PERCENTAGE)`

#### Stripe
I initially created my checkout form to have fields for “First Name” and “Last Name”. However, while trying to get my Stripe Webhooks working, I had an error come up to say “Received unknown parameters “first_name”, “last_name”. I realised this was because [Stripe](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-business) was expecting one name field to come through, not two. I initially fixed this by using the concatenate function in Javascipt to put the first name and last name fields together. However, I ended up deciding the easier way to fix this issue was to amend the Checkout Model to only have a field for “Name”.

#### Products Model – Shade
I wanted to add the option of users choosing different shades for products such as foundation. When learning how to create the Product model, I saw examples where the developer had a set list of “XS, S, M, L, XL” for all products, but I wanted to be able to have a different array for each product. To fix this issue, I found a field called “ArrayField” in the [Django Documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/fields/#arrayfield) that can have varying lengths, so that the shades can be iterated through. 


#### Back to Top Button
I created a back to top button, but wanted it to be invisible while the user is at the top of the page. I researched online and found a very helpful answer from Codesayan on [Stack Overflow](https://stackoverflow.com/questions/57229839/is-there-a-way-to-display-none-on-scroll-and-on-click)
I started by adding a function to make the Back to Top button display: none when the page loads. Then, when the user scroll is <= 100, the button staying in display:none. But if the user scroll is > 100, the button is shown.

#### Toasts
I originally tried to add the messages for toasts the way I had been taught, however I believe as I am using the most up-to-date version of Bootstrap, the following wouldn’t work:
```
$('.toast').toast('show');
```
 
I did some research on the [Code Institute Slack Community](https://code-institute-room.slack.com/archives/C026VTHQDNY/p1674258291733649) and found other students had been having the same issue. I was able to put together the following code which fixed my Toast’s not showing:
```
const lbToastList = $('.toast');
    for (let lbToast of lbToastList) {
        const toast = new bootstrap.Toast(lbToast);
        toast.show()
    }
 ```

 #### Shade ID

I was able to insert the shade straight into the ID of a span using Django templating, but the ID's still had spaces and capital letters since this is what is in the database. I started by adding `| lower` to the ID which sorted the case issue. Then I used jQuery to iterate through the spans, using the `.each()` function, found on the [jQuery documentation](https://api.jquery.com/each/). Lastly, I was able to use `.split()` and `.join()` to replace the spaces with hyphens. I found out how to do this from a helpful post on [Stack Overflow](https://stackoverflow.com/questions/1983648/replace-spaces-with-dashes-and-make-all-letters-lower-case).

After this, the shade's ID's were showing correctly - `#003 Moon` was now `#003-moon` - however I then encountered another issue. CSS ID's can't start with a number, so I moved the code I'd written into a variable called `oldShade`. Then, I created a new variable called `newShade` and set it equal to `"lb-" + oldShade` which fixed this issue.

#### Shades Preview

I wanted to add a couple of the shade to the product page, and then a third circle with the number of how many more shades availble there are. I tried to use `forloop.counter` in Django templating - as suggested in a [Stack Overflow](https://stackoverflow.com/questions/8659560/django-template-increment-the-value-of-a-variable) post, but I couldn't see an easy way to set a variable, then use `+=1` while iterating through the shades. Instead, I used `{% if forloop.first or forloop.last %}` to show two example shades. I also found a very interesting page on [Pypi](https://pypi.org/project/django-mathfilters/) that explained Django Math Filters. I was able to use Math Filters to subtract 2 from the length of the shades array, to show the user how many more shades Luna Beauty offers in for that product.

#### Footer

Most of my pages fill the page and push the footer to the bottom. However, after creating the Profile App I realised my footer was not sticking to the bottom of the page, regardless of the content height. I added a div with a class of "content" and used the [CSS Tricks](https://css-tricks.com/couple-takes-sticky-footer/) website to make sure my footer would stay at the very bottom of any page.

#### Email Apostrophes

I noticed when a user orders a product with an apostrophe in the name, such as "Lash 'n Roll" or L'Oréal, the confirmation email would have “L&#x27;Oreal" written on it instead. I researched and found a helpful page on [W3 Schools](https://www.w3schools.com/django/ref_tags_autoescape.php) where I found I could put `{% autoescape on %}` and `{% endautoescape %}`, and this would display the apostrophe as it should be.

#### Save Info

My "Save Info" checkbox was working if a user wants to save their info to their account. However, if they unchecked the box, the profile details were still being overwritten. I put print statements before each time "save_info" was used, and found two were showing up as "True" when the checkbox was unchecked. I fixed these by adding `if save_info != "false":` to the handle_payment_intent_succeeded function in webhook_handler.py. However, this didn't fix the issue. I also tried calling the stripe_elements.js file in `{% block extra_js %}` instead of `{% block postload_js %}`, as suggested on [this post](https://app.slack.com/client/T0L30B202/C7HS3U3AP/1605302104.469800) in the Code Institute Slack community, but this didn't fix the issue either.

I spoke to the Tutor Support team for Code Institute and found that the "save_info" session variable wasn't being deleted after the profile had previously been overwritten. I was able to fix this by adding `del request.session['save_info']` to the checkout_success function in views.py in the Checkout app, after the if statement to check whether "save_info" was true or false.

#### Django Testing

After writing my Django tests in the Checkout and Product apps, I was having problems running the tests. I spoke to a member of the Code Institute support team and we figured out that I'm been running my database in PostgreSQL because the ArrayField in my Product app is not supported by SQLite3. I amended the models to:

```
    if 'DEVELOPMENT' in os.environ:
        shades = models.TextField(max_length=200, null=True, blank=True)
    else:
        shades = ArrayField(models.CharField(max_length=200), null=True, blank=True)
```

I also commented out my Database URL in env.py, and deleted my migrations as they referenced the ArrayField. Once this was complete, I was able to migrate the changes in SQLite3. I wrote and ran my tests, which all came up as successful.

Once I was done with testing, I deleted the migration file in the Products app, and uncommented the Database URL in env.py. I tried to migrate again but kept getting another error:

`Migration checkout.0001_initial dependencies reference nonexistent parent node ('products', '0001_initial')`

I searched the internet and struggled for a while with this issues. I tried creating a new workspace from the last commit, to see if I could replicate where the code went wrong. I added my testing documents to this new workspace and commit the changes, with the idea of writing the issue up in my fixed bugs. 

I tried to migrated this new version, but when creating a superuser, an error came up that said:

`django.db.utils.OperationalError: no such column: profiles_userprofile.default_name`

After taking a break, I decided to try fixing the original file once more, as I'd realised I still had migrations that hadn't been deleted. I deleted all migrations and found I was then able to migrate properly, and I could run the SQLite3 database, and pass all the tests. I also found I'd got the development version of the project to work in port 8000.

I tried to commit my changes, but as I had committed from a different workspace, I had to use `git pull original main`. There was a discrepancy between the two test.py files in the Product apps. The change was one had an extra blank line, so I used `git merge` to fix this issue, and was then able to commit my new changes.
 
## Unfixed Bugs

#### Django Testing (continued)

Due to using the ArrayField in models.py in the Proucts app, I am unable to use SQLite3 in Development mode. This means each time I need to access Development mode, if I create a new workspace I would need to add the PostgreSQL Database URL to my env.py.

#### Shades

Each shade in the products app has a corresponding ID. In shades.css I've created an individual background colour hex for each shade, to give users the most accurate colour choice when selecting their shade for foundations or lipsticks. However, currently there is no way for an Admin to add the hex to the shades.css, so this would need to be added the developer. As a future feature, I would like to change this so the Admin can add their shades, and the corresponding HEX colour could be added to shades.css.

## Deployment
I managed to deploy the website without any issues, and all my links worked perfectly. I used the following steps to achieve this:

1. I created an account on Heroku for deploying the site, and ElephantSQL to host my database.
2. I created the database on ElephantSQL using the "Create new instance", giving the project a name and selecting my plan and location.
3. Then I created a requirements.txt file, and a Procfile, both of which are needed to deploy on Heroku.
4. I used the "Create new app" button on Heroku and gave my project a name.
5. I copied the URL from my ElephantSQL project and applied it as a Config Var under the Settings tab on Heroku.
6. I added the rest of the variables from my env.py file to my Config Vars section on Heroku.
7. I changed to the Deploy tab on Heroku, and clicked on Connect to Github.
8. I enabled automatic deploys and deployed from the main branch.
9. I built my database by migrating my models to PostgreSQL, then using `python3 manage.py loaddata` for `categories` and `products`.
10. I created a new superuser, and an AWS Account.
11. I used AWS to host my Media and Static files by using S3, and created Users, Groups and Policies before uploading the files to the relevant folder.
10. I checked my project had successfuly deployed using the "Open App" button on Heroku.

## Credits

#### Technologies
* [Django](https://www.djangoproject.com/)
    * Project Framework

* [Stripe](https://stripe.com/gb)
    * Take payments in the Checkout app

* [SQLite3](https://www.sqlite.org/)
    * Development Database

* [ElephantSQL](https://www.elephantsql.com/)
    * Production Database

* [Heroku](https://heroku.com/)
    * Deployment

* [Figma](https://www.figma.com/)
    * Wireframes
    * Prototype

* [Bootstrap](https://getbootstrap.com/)
    * Grid styling
    * Toast styling
    * Navbar for all sized screens
    * Buttons
    * Checkbox
    * Card Styling

* [Font Awesome](https://fontawesome.com/)
    * Social Media icons
    * Button double arrows
    * Bag icon on navbar
    * Info, Success, Warning and Error toast icons

* [Google Fonts](https://fonts.google.com/)
    * Noto
    * Jost

* [Favicon Converter](https://favicon.io/favicon-converter/)
    * Moon Favicon

#### Code
* [Random Number Generator](https://www.random.org/integers/?num=45&min=100000000&max=999999999&col=5&base=10&format=html&rnd=new)
    * Creating Product SKU's

* [Stack Overflow](https://stackoverflow.com/)
    * See [Fixed Bugs](#fixed-bugs) section

#### Media
* [Am I Responsive image](https://amiresponsive.blogspot.com/)
* [Purple clouds behind the discount offer](https://www.pexels.com/photo/purple-sky-1287142/)
* [Three eyeshadow palettes on the home page](https://www.pexels.com/photo/three-black-square-makeup-palettes-2639947/)
* [Photo of a woman with make up on the home page](https://pixabay.com/photos/woman-portrait-face-skin-make-up-3096664/)
* [Logo created by me on Canva](https://www.canva.com/en_gb/)
* [Favicon created by me on Canva](https://www.canva.com/en_gb/)
* Prototype Images
    * [Face with eyeshadow](https://www.pexels.com/photo/close-up-photo-of-woman-with-pink-eyeshadow-3912572/)
    * [Close up of eyeshadow palette](https://pixabay.com/photos/makeup-palette-colorful-eyeshadow-1138857/)
    * [Eyeshadow colours and brushes](https://www.pexels.com/photo/colored-powders-and-brush-1749452/)
    * [Assorted lipgloss colours](https://www.pexels.com/photo/five-assorted-color-of-liquid-lipsticks-3373738/)

#### Product Images, Shades and Descriptions

##### Face
* L'Oréal Paris True Match Liquid Foundation
    * [Boots](https://www.boots.com/loreal-paris-true-match-foundation-30ml-10200787)
    * [Loreal Paris](https://www.loreal-paris.co.uk/true-match/foundation)

* e.l.f. Halo Glow Liquid Filter
    * [Boots](https://www.boots.com/elf-halo-glow-liquid-filter-10318554)
    * [Beauty Bay](https://www.beautybay.com/p/elf-cosmetics/halo-glow-liquid-filter/ )

* NARS Sheer Glow Foundation
    * [Boots](https://www.boots.com/nars-sheer-glow-foundation-10286863)
    * [Nars Cosmetics](https://www.narscosmetics.co.uk/en/sheer-glow-foundation/999NACSGLWF01.html?cgid=Discover&bvstate=pg:53/ct:r)

* Estée Lauder Double Wear Stay-in-Place Foundation
    * [Boots](https://www.boots.com/estee-lauder-double-wear-stay-in-place-makeup-spf-10-30ml-10249140)

* MAC Studio Fix Fluid Spf15 Foundation
    * [Beauty Bay](https://www.beautybay.com/p/mac-cosmetics/studio-fix-fluid-spf15-foundation/nw20/)

* Makeup Revolution Conceal & Define Foundation
    * [Beauty Bay](https://www.beautybay.com/p/makeup-revolution/conceal-and-define-foundation/f2/)

##### Lips
* e.l.f Glow Reviver Lip Oil
    * [Beauty Bay](https://www.beautybay.com/p/elf-cosmetics/glow-reviver-lip-oil/honey-talks/)

* MAC Matte Lipstick
    * [Beauty Bay](https://www.beautybay.com/p/mac-cosmetics/matte-lipstick/marrakesh/)

* L'Oreal Paris Color Riche Satin Lipstick
    * [Boots](https://www.boots.com/loreal-paris-color-riche-satin-lipstick-10248257)
    * [Loreal Paris](https://www.loreal-paris.co.uk/color-riche/satin/lipstick-303-rose-tendre)

* NYX Professional Makeup Butter Lip Gloss
    * [Boots](https://www.boots.com/nyx-professional-makeup-butter-gloss-10207772)
    * [NXY Cosmetics](https://www.nyxcosmetics.co.uk/lips-makeup/lip-gloss/butter-gloss-lip-gloss/NYX_089.html?dwvar_NYX__089_color=Sorbet)

* Maybelline Lifter Gloss Hydrating Lip Gloss
    * [Boots](https://www.boots.com/maybelline-lifter-gloss-plumping-hydrating-lip-gloss-hyaluronic-acid-10292293)
    * [Maybelline](https://www.maybelline.co.uk/all-products/lip-makeup/lip-gloss/lifter-gloss-lip-gloss-makeup-with-hyaluronic-acid?variant=Moon)

* Clinique Pop Plush Creamy Lip Gloss
    * [Beauty Bay](https://www.beautybay.com/p/clinique/pop-plush-creamy-lip-gloss/pink-gimlet/)

##### Eyes

* Maybelline Lash Sensational Sky High Mascara
    * [Beauty Bay](https://www.beautybay.com/p/maybelline/lash-sensational-sky-high-mascara/lash-sensational-sky-high-mascara/)
    * [Maybelline](https://www.maybelline.co.uk/all-products/eye-makeup/mascara/lash-sensational-sky-high-washable-mascara-makeup?variant=Blue+Mist)

* e.l.f. Lash 'n Roll Curling Mascara
    * [Beauty Bay](https://www.beautybay.com/p/elf-cosmetics/lash-n-roll-curling-mascara/)

* Maybelline Lash Sensational Mascara Intense Black
    * [Beauty Bay](https://www.beautybay.com/p/maybelline/lash-sensational-mascara-intense-black/)

* Urban Decay Perversion Mascara
    * [Beauty Bay](https://www.beautybay.com/p/urban-decay/perversion-mascara/)

* Clinique High Impact Mascara
    * [Beauty Bay](https://www.beautybay.com/p/clinique/high-impact-mascara/black/)
    * [Clinique](https://www.clinique.co.uk/product/1606/5416/makeup/mascara/high-impacttm-mascara)

* Revlon ColorStay Day to Night Eyeshadow Quad Pretty
    * [Boots](https://www.boots.com/revlon-colorstay-16-hour-eyeshadow-palette-10137952)
    * [Sainsburys](https://www.sainsburys.co.uk/gol-ui/product/revlon-colorstay-day-to-night-eyeshadow-quad-stunning-48g)

* Max Factor Masterpiece Nude Eyeshadow Palette Rose Nudes
    * [Boots](https://www.boots.com/max-factor-masterpiece-nude-eyeshadow-palette-rose-nudes-10298639)
    * [Superdrug](https://www.superdrug.com/make-up/eye-makeup/eye-shadow/eye-shadow-palettes/max-factor-masterpiece-nude-palette-003-rose-nudes/p/807480)

* Urban Decay Naked 3 Mini Eyeshadow Palette
    * [Boots](https://www.boots.com/urban-decay-naked-3-mini-eyeshadow-palette-10318139)

* No7 Limited Edition Pink Collection Eyeshadow Quad
    * [Boots](https://www.boots.com/no7-limited-edition-pink-collection-eyeshadow-quad-10338258)

* NYX Professional Makeup Ultimate Shadow Palette Vegan 16-Pan Warm Neutrals
    * [Boots](https://www.boots.com/nyx-professional-make-up-ultimate-shadow-palette-vegan-16-pan---warm-neutrals-10334185)

* e.l.f. Bite-Size Eyeshadow Palette I Love You A Latte
    * [Beauty Bay](https://www.beautybay.com/p/elf-cosmetics/bite-size-eyeshadow-palette-i-love-you-a-latte/)

* Max Factor Color Xpert Soft Touch Palette 004 - Veiled Bronze
    * [Boots](https://www.boots.com/max-factor-color-xpert-soft-touch-palette-veiled-bronze-10290538)

##### Cheeks

* Benefit Mini Dandelion Baby-Pink Brightening Blush
    * [Boots](https://www.boots.com/benefit-mini-dandelion-baby-pink-brightening-blush-2-5g-10315037)

* L'Oreal Paris Blush of Paradise Melon Dollar Baby
    * [Boots](https://www.boots.com/loreal-paris-blush-of-paradise-melon-dollar-baby-10295638)

* Clinique Blushing Blush Powder Blush
    * [Boots](https://www.boots.com/clinique-blushing-blush-powder-blush-6g-10047580)

* bareMinerals Gen Nude Blushlighter
    * [Boots](https://www.boots.com/bareminerals-gen-nude-blushlighter-10328161)

* e.l.f. Primer-Infused Bronzer
    * [Beauty Bay](https://www.beautybay.com/p/elf-cosmetics/primer-infused-bronzer/)

* MAC Mineralize Blush Warm Soul
    * [Beauty Bay](https://www.beautybay.com/p/mac-cosmetics/mineralize-blush/warm-soul/)

* NXY Highlight and Contour Pro Palette
    * [Beauty Bay](https://www.beautybay.com/p/nyx-professional-makeup/highlight-and-contour-pro-palette/)

## Acknowledgements
* The fantastic Student Support Team at Code Institute
* My City of Bristol College Tutors