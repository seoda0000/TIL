package com.example.sd_lecture

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {

//        화면을 보여주는 코드
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        1. 화면이 클릭되었다는 것을 알아야 한다
        val image1 = findViewById<ImageView>(R.id.sd_image_1)
        val image2 = findViewById<ImageView>(R.id.sd_image_2)
        val image3 = findViewById<ImageView>(R.id.sd_image_3)
        val image4 = findViewById<ImageView>(R.id.sd_image_4)
        val image5 = findViewById<ImageView>(R.id.sd_image_5)
        val image6 = findViewById<ImageView>(R.id.sd_image_6)
        val image7 = findViewById<ImageView>(R.id.sd_image_7)
        val image8 = findViewById<ImageView>(R.id.sd_image_8)

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

        
    }
}