private fun updateBottomMenu(navigation: BottomNavigationView) {
        val tag1: Fragment? = supportFragmentManager.findFragmentByTag("pot")
        val tag2: Fragment? = supportFragmentManager.findFragmentByTag("search")
        val tag3: Fragment? = supportFragmentManager.findFragmentByTag("community")
        val tag4: Fragment? = supportFragmentManager.findFragmentByTag("user")
        Log.d(TAG, "${tag1} ${tag2} ${tag3} ${tag4}")

        if (tag1 != null && tag1.isVisible()) navigation.getMenu().findItem(R.id.potFragment)
            .setChecked(true)
        else if (tag2 != null && tag2.isVisible()) navigation.getMenu()
            .findItem(R.id.searchFragment).setChecked(true)
        else if (tag3 != null && tag3.isVisible()) navigation.getMenu()
            .findItem(R.id.communityFragment).setChecked(true)
        else if (tag4 != null && tag4.isVisible()) navigation.getMenu().findItem(R.id.userFragment)
            .setChecked(true)
        else {

//            스택 아무것도 없을 때 인트로로
            val tag5: Fragment? = supportFragmentManager.findFragmentByTag("pot_diary")
            val tag6: Fragment? = supportFragmentManager.findFragmentByTag("pot_diary_create")
            val tag7: Fragment? = supportFragmentManager.findFragmentByTag("pot_detail")
            val tag8: Fragment? = supportFragmentManager.findFragmentByTag("search_detail")
            val tag9: Fragment? = supportFragmentManager.findFragmentByTag("community_share")
            val tag10: Fragment? = supportFragmentManager.findFragmentByTag("community_post")
            val tag11: Fragment? = supportFragmentManager.findFragmentByTag("setting")

            if (tag5 == null && tag6 == null && tag7 == null && tag8 == null && tag9 == null && tag10 == null && tag11 == null) {
                var intent = Intent(this, IntroActivity::class.java)
                startActivity(intent)
            }
        }
    }