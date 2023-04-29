package com.example.sd_lecture

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.widget.ImageView
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import com.example.sd_lecture.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    //    데이터 바인딩 사용하기
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {

//        화면을 보여주는 코드
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        리스트
        var testList = mutableListOf<String>()
        testList.add("a")
        testList.add("b")
        testList.add("c")
        Log.d("MainActivity", testList[0])


//        로그 찍기
        val test = "테스트 값이에요"
        Log.d("MainActivity", "testLog")
        Log.e("MainActivity", test)
        Log.w("MainActivity", test)
        Log.i("MainActivity", test)
        Log.d("MainActivity", test)
        Log.v("MainActivity", test)

        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.mainBtn.setOnClickListener {
            var intent = Intent(this, DiceActivity::class.java)
            startActivity(intent)
        }
        binding.lstBtn.setOnClickListener {
            var intent = Intent(this, ListViewActivity::class.java)
            startActivity(intent)
        }

//        1. 화면이 클릭되었다는 것을 알아야 한다
        val image1 = findViewById<ImageView>(R.id.sd_image_1)
        val image2 = findViewById<ImageView>(R.id.sd_image_2)
        val image3 = findViewById<ImageView>(R.id.sd_image_3)
        val image4 = findViewById<ImageView>(R.id.sd_image_4)
        val image5 = findViewById<ImageView>(R.id.sd_image_5)
        val image6 = findViewById<ImageView>(R.id.sd_image_6)
        val image7 = findViewById<ImageView>(R.id.sd_image_7)
        val image8 = binding.sdImage8

        image1.setOnClickListener {

            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "1")
            startActivity(intent)
        }
        image2.setOnClickListener {

            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "2")
            startActivity(intent)
        }
        image3.setOnClickListener {

            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "3")
            startActivity(intent)
        }
        image4.setOnClickListener {


            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "4")
            startActivity(intent)
        }
        image5.setOnClickListener {


            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "5")
            startActivity(intent)
        }
        image6.setOnClickListener {


            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "6")
            startActivity(intent)
        }
        image7.setOnClickListener {


            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "7")
            startActivity(intent)
        }
        image8.setOnClickListener {


            var intent = Intent(this, SD1Activity::class.java)
            intent.putExtra("data", "8")
            startActivity(intent)
        }


//        변수 종류 알아보기
        var value = "var은 바꿀 수 있습니다"
        val value2 = "val은 바꿀 수 없습니다"


    }
//    back button 설정

    private var isDouble = false
    override fun onBackPressed() {

        if (isDouble == true) {
            finish()
        }

        isDouble = true
        Toast.makeText(this, "종료하시려면 더블클릭", Toast.LENGTH_LONG).show()

        Handler().postDelayed(Runnable {
            isDouble = false
        }, 2000)

    }
}