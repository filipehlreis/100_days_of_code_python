from instagramfollowers import InstagramFollowersBot


if __name__ == "__main__":
    USER = "instagram"
    USER = "facebookapp"
    USER = "waze"

    bot = InstagramFollowersBot()

    bot.login()
    bot.find_followers(USER)
    bot.follow()

    # bot.driver.close()
