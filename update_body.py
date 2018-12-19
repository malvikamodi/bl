import datetime
date = datetime.datetime.today().strftime('%Y-%m-%d')


body_sb_add = {"script": {
    "lang": "painless",
    "source" : """
      if (ctx._source.blacklists == null)
      {
        ctx._source.blacklists = new HashMap();
      }

      if (ctx._source.blacklists.safebrowsing == null)
      {
        ctx._source.blacklists.safebrowsing = new HashMap();
        ctx._source.blacklists.safebrowsing.blacklist_add_history = [];
        ctx._source.blacklists.safebrowsing.blacklist_remove_history = [];
      }

      ctx._source.blacklists.safebrowsing.is_blacklisted = true;
      ctx._source.blacklists.safebrowsing.blacklist_add_history.add(params.time);
    """,
    "params": {
      "time": date,
    }
  }
}

body_phishtank_add= {"script": {
    "lang": "painless",
    "source" : """
      if (ctx._source.blacklists == null)
      {
        ctx._source.blacklists = new HashMap();
      }

      if (ctx._source.blacklists.phishtank == null)
      {
        ctx._source.blacklists.phishtank = new HashMap();
        ctx._source.blacklists.phishtank.blacklist_add_history = [];
        ctx._source.blacklists.phishtank.blacklist_remove_history = [];
      }

      ctx._source.blacklists.phishtank.is_blacklisted = true;
      ctx._source.blacklists.phishtank.blacklist_add_history.add(params.time);
    """,
    "params": {
      "time": date,
    }
  }
}

body_sb_remove = {"script": {
    "lang": "painless",
    "source" : """
      ctx._source.blacklists.safebrowsing.is_blacklisted = false;
      ctx._source.blacklists.safebrowsing.blacklist_remove_history.add(params.time);
    """,
    "params": {
      "time": date,
    }
  }
}

body_phishtank_remove = {"script": {
    "lang": "painless",
    "source" : """
      ctx._source.blacklists.phishtank.is_blacklisted = false;
      ctx._source.blacklists.phishtank.blacklist_remove_history.add(params.time);
    """,
    "params": {
      "time": date,
    }
  }
}
