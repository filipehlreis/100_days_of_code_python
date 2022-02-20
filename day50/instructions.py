"""
Step 1 - Setup your account on Tinder
1. If you don't already have an account on Tinder, set one up now. Make sure
you can sign in to your account using Facebook or Google.

If you don't want to use your own details, ask a friend who is on Tinder or
just set up a new Facebook account and use an AI-generated image from https:
// www.thispersondoesnotexist.com/

HINT: You can hit refresh on thispersondoesnotexist to generate new random
images.

2. Manually go through the process of swiping on profiles and see which
elements you'll need to target with your code.

NOTE: If you don't want to disappoint anyone (I'm sure you are very
attractive/good dating material 😜), you can always complete the tutorial
and hit "NOPE" on everyone. Least you break people's hearts by matching
with them and then telling them "Sorry I just did it for a Python tutorial" 😢.




Step 2 - Navigate to Login Page
In order to avoid dual verification with a phone every time we log in,
we'll need to use the Facebook/Google login. The Google login flow requires
a lot more steps than Facebook login, so we'll go with Facebook in this
challenge.

1. Using Selenium and Python Navigate to the Tinder website
(https://tinder.com/) and click on LOG IN then LOGIN WITH FACEBOOK. See below:
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-09-13-
c82d3512f06309199abbd002ce971f31.png

If successful, you should see a pop-up for Facebook login:
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-14-05-
a9c66cf9149f34720e387144bd02c6fc.png

HINT 1: Make sure you've already manually signed-in and verified your
phone number with Tinder as we can't automate the phone number verification.
You only have to do this once.

HINT 2: If you are getting a NoSuchElementException, make sure you've
added some delay between clicking on buttons so that the new element has
enough time to load.

HINT 3: You might find it easier to right click on the element and get the
XPath to use with Selenium. e.g.

https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-17-01-
2cdd16603c955114c440cb5ff8e94e95.png








Step 3 - Login with Facebook
1. The Facebook login page opens in a new window. In order for our selenium
code to work on the new window, we have to switch to the window in front.

In Selenium, each window has a identification handle, we can get all the
window handles with:

driver.window_handles

The above line of code returns a list of all the window handles. The first
window is at position 0 e.g.

base_window = driver.window_handles[0]

New windows that have popped out from the base_window are further down in
the sequence e.g.

fb_login_window = driver.window_handles[1]

We can switch our Selenium to target the new facebook login window by:

driver.switch_to.window(fb_login_window)

You can print the driver.title to verify that it's the facebook login window
that is currently target:

print(driver.title)

The full code to switch to the new pop-up window is thus:

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

If successful the printed title should be "Facebook" and not
"Tinder | Match. Chat. Date."



2.  Using what you have learnt about Selenium, fill in the Facebook login
form and submit it to log in.
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-33-57-
3f82315199d6c26b232010d4be600fd1.png

NOTE: Avoid invoking the Facebook Login too frequently, see if you can test
your code without logging in, you don't want to appear like a bot to Facebook
as there is always the chance that they might disable your FB account.
Alternatively, you can try setting up an alternative Facebook account.

If successful, you should see the pop-up window disappear and you're back
on the Tinder page. e.g.
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-36-03-
c39aaf979df1854cc259aebafd8a2ae7.png



3. At this point, you should revert back to the base_window and verify by
printing the title of the Selenium controlled window title.

driver.switch_to.window(base_window)
print(driver.title)

If successful, it should print "Tinder | Match. Chat. Date."






Step 4 - Dismiss all requests
When you first login to Tinder, it will ask if it's ok to get your location,
send you notifications and track your cookies. We need to dismiss all of
these modal pop-ups.

Location Pop-up:
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-43-00-
49d934f6791bf4bad82b5438baa025e3.png

Notification Pop-up:
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-43-16-
4cee84dbd662e94e2d76238197f7b572.png

Cookies Pop-up:
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-43-45-
70a2a3812ac11797f8767a6529da9aa8.png

1. Using Selenium and Python:

- Click ALLOW for location.

- Click NOT INTERESTED for notifications.

- Click I ACCEPT for cookies

HINT 1: Finding the XPath will make it easier to target each element.

HITN 2: Adding some delay before targeting these elements will allow time
for them to load up.






Step 5 - Hit Like!
1. The final step is to like some people. Because it's the web version, we
don't have to swipe right, all we need to do is to click on the "Like"
button. You'll want to add at least a 1 second delay between "Likes" so that
Tinder doesn't block you because you seem like a bot.
https://img-c.udemycdn.com/redactor/raw/2020-08-21_15-49-34-
7a1f2a27c14e05ceaa2f7833f79b7870.png

HINT 1: It takes a while for Tinder to load up people near you, this is not
a fixed time as it depends on a number of factors. When it's loading, the
"Like" button will not be reachable and you will get a NoSuchElementException
if you try to find it. Use exception handling to handle this situation and
wait 2 seconds before you retry.

HINT 2: Sometimes, as you are swiping, you'll get a match which is a pop-up
on the same page. But this will mean that your Like button will be hidden
behind the pop up and you'll get a ElementClickInterceptedException. e.g.
https://img-c.udemycdn.com/redactor/raw/2020-08-24_08-22-53-
eef36c0698acfe67157d5ffcee6c9749.png

You'll need to dismiss this by clicking on "BACK TO TINDER" to continue
swiping.

NOTE: On the free tier, Tinder only allows 100 "Likes" per day.



"""
