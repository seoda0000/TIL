package com.example.sd_lecture

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView
import android.widget.Toast

class SD1Activity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sd1)

        val getData = intent.getStringExtra("data")

        val bookImage = findViewById<ImageView>(R.id.bookImageArea)

//        Toast.makeText(this, getData, Toast.LENGTH_LONG).show()
        if(getData == "1") {
            bookImage.setImageResource(R.drawable.sd1)
        }
        if(getData == "2") {
            bookImage.setImageResource(R.drawable.sd2)
        }
        if(getData == "3") {
            bookImage.setImageResource(R.drawable.sd3)
        }
        if(getData == "4") {
            bookImage.setImageResource(R.drawable.sd4)
        }
        if(getData == "5") {
            bookImage.setImageResource(R.drawable.sd5)
        }
        if(getData == "6") {
            bookImage.setImageResource(R.drawable.sd6)
        }
        if(getData == "7") {
            bookImage.setImageResource(R.drawable.sd7)
        }
        if(getData == "8") {
            bookImage.setImageResource(R.drawable.sd8)
        }
    }

}