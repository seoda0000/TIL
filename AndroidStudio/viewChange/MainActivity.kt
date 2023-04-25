package com.chocobi.groot

import android.content.ContentValues
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.util.Log
import android.widget.Toast
import androidx.core.app.ActivityCompat
import com.chocobi.groot.databinding.ActivityMainBinding
import com.chocobi.groot.view.community.CommunityFragment
import com.chocobi.groot.view.community.CommunityPostFragment
import com.chocobi.groot.view.community.CommunityShareFragment
import com.chocobi.groot.view.plant.PlantDiaryFragment
import com.chocobi.groot.view.plant.PlantFragment
import com.chocobi.groot.view.search.SearchCameraActivity
import com.chocobi.groot.view.search.SearchDetailFragment
import com.chocobi.groot.view.search.SearchFragment
import com.chocobi.groot.view.user.SettingFragment
import com.chocobi.groot.view.user.UserFragment
import com.google.android.material.bottomnavigation.BottomNavigationView
import java.text.SimpleDateFormat

class MainActivity : AppCompatActivity() {
    //    private lateinit var binding: ActivityMainBinding
    private val PERMISSION_CAMERA = 0
    private val REQUEST_CAMERA = 1

    //        fragment 조작
    fun changeFragment(index: String) {
        when (index) {
            "plant_diary" -> {
                val plantDiaryFragment = PlantDiaryFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, plantDiaryFragment)
                    .commit()
            }

            "search" -> {
                val searchFragment = SearchFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, searchFragment)
                    .commit()
            }

            "search_detail" -> {
                Log.d("MainActivity", "search detail 호출")
                val searchDetailFragment = SearchDetailFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, searchDetailFragment)
                    .commit()
            }

            "community_share" -> {
                val communityShareFragment = CommunityShareFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, communityShareFragment)
                    .commit()
            }

            "community_post" -> {
                val communityPostFragment = CommunityPostFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, communityPostFragment)
                    .commit()
            }

            "setting" -> {
                val settingFragment = SettingFragment()
                supportFragmentManager
                    .beginTransaction()
                    .replace(R.id.fl_container, settingFragment)
                    .commit()
            }
        }
    }

   

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)



//        네비게이션 바 조작
        // 하단 탭이 눌렸을 때 화면을 전환하기 위해선 이벤트 처리하기 위해 BottomNavigationView 객체 생성
        var bnv_main = findViewById(R.id.bottom_navigation) as BottomNavigationView

        // OnNavigationItemSelectedListener를 통해 탭 아이템 선택 시 이벤트를 처리
        // navi_menu.xml 에서 설정했던 각 아이템들의 id를 통해 알맞은 프래그먼트로 변경하게 한다.
        bnv_main.run {
            setOnNavigationItemSelectedListener {
                when (it.itemId) {
                    R.id.plantFragment -> {
                        // 다른 프래그먼트 화면으로 이동하는 기능
                        val homeFragment = PlantFragment()
                        supportFragmentManager.beginTransaction()
                            .replace(R.id.fl_container, homeFragment).commit()
                    }

                    R.id.searchFragment -> {
                        val boardFragment = SearchFragment()
                        supportFragmentManager.beginTransaction()
                            .replace(R.id.fl_container, boardFragment).commit()
                    }

                    R.id.communityFragment -> {
                        val boardFragment = CommunityFragment()
                        supportFragmentManager.beginTransaction()
                            .replace(R.id.fl_container, boardFragment).commit()
                    }

                    R.id.userFragment -> {
                        val boardFragment = UserFragment()
                        supportFragmentManager.beginTransaction()
                            .replace(R.id.fl_container, boardFragment).commit()
                    }
                }
                true
            }
            selectedItemId = R.id.plantFragment
//            1차 릴리즈 : search를 메인으로
//            selectedItemId = R.id.searchFragment
        }

        //        특정 프레그먼트로 이동
        var toPage = intent.getStringExtra("toPage")
        Log.d("MainActivity", "onCreate")
        if (toPage == "search_detail") {
            Log.d("MainActivity", "toPage" + toPage)
            bnv_main.run { selectedItemId = R.id.searchFragment }
            changeFragment(toPage)
        }
    }


}


