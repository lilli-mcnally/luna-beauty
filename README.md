# Luna Beauty

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

In the future I would like to add the option to review items. I'd also like to expand the range to include skincare, and add blog pages about recommendations for products.

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

## Unfixed Bugs

There are no unfixed bugs to my knowledge.