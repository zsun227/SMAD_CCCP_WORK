CREATE EXTERNAL TABLE covid_rc_1(

	created_at string,
   id_str string,
   truncated boolean,
   in_reply_to_screen_name string,
   in_reply_to_status_id_str string,
   in_reply_to_user_id_str string,
   text string,
   source string,
   favorited boolean,
   retweeted boolean,
   lang string,
   timestamp_ms string,

   coordinates string, 
  
   place string, 

   extended_tweet struct < 
      full_text: string >,

   quote_count string,
   reply_count string,
   retweet_count string, 
   favorite_count string, 
   is_quote_status boolean, 
   quoted_status_id string,
   quoted_status_id_str string, 


   quoted_status_permalink struct < 
      url: string,
      expanded: string,
      display: string>,

   
   quoted_status struct < 
      created_at: string,
      id: string,
      id_str: string,
      text: string, 
      source: string, 
      truncated: boolean,
      is_quote_status: boolean,
      quote_count: string,
      reply_count :  string,
      retweet_count  :  string,
      favorite_count :  string,

      user: struct <
         contributors_enabled: boolean,
         created_at: string,
         default_profile: boolean,
         default_profile_image: boolean,
         description: string,
         favourites_count: string,
         followers_count: string,
         friends_count: string,
         geo_enabled: boolean,
         id: string,
         id_str: string,
         is_translator: boolean,
         lang: string,
         listed_count: string,
         name: string,
         `location`: string, 
         profile_background_color: string,
         profile_background_image_url: string,
         profile_background_image_url_https: string,
         profile_background_tile: boolean,
         profile_banner_url: string,
         profile_image_url: string,
         profile_image_url_https: string,
         profile_link_color: string,
         profile_sidebar_border_color: string,
         profile_sidebar_fill_color: string,
         profile_text_color: string,
         profile_use_background_image: boolean,
         protected: boolean,
         screen_name: string,
         statuses_count: string,
         time_zone: string,
         url: string,
         utc_offset: string,
         verified: boolean>>, 

	entities struct <
      hashtags: array <struct <text: string>>,

      urls: array <struct <
            	display_url: string,
            	expanded_url: string,
            	url: string>>,

      user_mentions: array <struct <
            	id: string,
            	name: string,
            	screen_name: string>>>,

	user struct <
      contributors_enabled: boolean,
      created_at: string,
      default_profile: boolean,
      default_profile_image: boolean,
      description: string,
      favourites_count: string,
      followers_count: string,
      friends_count: string,
      geo_enabled: boolean,
      id: string,
      id_str: string,
      is_translator: boolean,
      lang: string,
      listed_count: string,
      name: string,
      `location`: string, 
      profile_background_color: string,
      profile_background_image_url: string,
      profile_background_image_url_https: string,
      profile_background_tile: boolean,
      profile_banner_url: string,
      profile_image_url: string,
      profile_image_url_https: string,
      profile_link_color: string,
      profile_sidebar_border_color: string,
      profile_sidebar_fill_color: string,
      profile_text_color: string,
      profile_use_background_image: boolean,
      protected: boolean,
      screen_name: string,
      statuses_count: string,
      time_zone: string,
      url: string,
      utc_offset: string,
      verified: boolean>,

	retweeted_status struct <
      extended_tweet: struct < 
      full_text: string >,

      quote_count: string,
      reply_count: string,
      retweet_count: string, 
      favorite_count: string, 
      is_quote_status: boolean, 
      quoted_status_id: string,
      quoted_status_id_str: string, 

      created_at: string,

      entities: struct <
         hashtags: array <struct <
               text: string>>,
         urls: array <struct <
               display_url: string,
               expanded_url: string,
               url: string>>,
         user_mentions: array <struct <
               id: string,
               name: string,
               screen_name: string>>>,

      favorited: boolean,

      id_str: string,
      in_reply_to_screen_name: string,
      in_reply_to_status_id_str: string,
      in_reply_to_user_id_str: string,


      possibly_sensitive: boolean,

      source: string,
      text: string,
      truncated: boolean,
      extended_tweet: struct < 
         full_text: string >,

      user: struct <
         contributors_enabled: boolean,
         created_at: string,
         default_profile: boolean,
         default_profile_image: boolean,
         description: string,
         favourites_count: string,
         followers_count: string,
         friends_count: string,
         geo_enabled: boolean,
         id: string,
         id_str: string,
         is_translator: boolean,
         lang: string,
         listed_count: string,
         name: string,
         `location`: string, 
         profile_background_color: string,
         profile_background_image_url: string,
         profile_background_image_url_https: string,
         profile_background_tile: boolean,
         profile_banner_url: string,
         profile_image_url: string,
         profile_image_url_https: string,
         profile_link_color: string,
         profile_sidebar_border_color: string,
         profile_sidebar_fill_color: string,
         profile_text_color: string,
         profile_use_background_image: boolean,
         protected: boolean,
         screen_name: string,
         statuses_count: string,
         time_zone: string,
         url: string,
         utc_offset: string,
         verified: boolean>>
)
PARTITIONED BY (year INT, month INT, day INT, hour INT, ind INT)
STORED AS rcfile
LOCATION '/user/zhongkai/covid_rc_1';

