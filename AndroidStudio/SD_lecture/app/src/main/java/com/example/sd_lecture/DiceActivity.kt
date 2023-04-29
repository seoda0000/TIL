package com.example.sd_lecture

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import com.example.sd_lecture.databinding.ActivityDiceBinding
import com.example.sd_lecture.databinding.ActivityMainBinding
import kotlin.random.Random

class DiceActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDiceBinding

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dice)

        binding = DataBindingUtil.setContentView(this, R.layout.activity_dice)

        val diceImage1 = binding.diceImage1
        val diceImage2 = binding.diceImage2

        binding.diceStartBtn.setOnClickListener {
            Toast.makeText(this, "주사위 Go!", Toast.LENGTH_LONG).show()
            val number1 = Random.nextInt(1, 6)
            val number2 = Random.nextInt(1, 6)

            if (number1 == 1) {
                diceImage1.setImageResource(R.drawable.dice1)
            } else if (number1 == 2) {
                diceImage1.setImageResource(R.drawable.dice2)
            }else if (number1 == 3) {
                diceImage1.setImageResource(R.drawable.dice3)
            }else if (number1 == 4) {
                diceImage1.setImageResource(R.drawable.dice4)
            }else if (number1 == 5) {
                diceImage1.setImageResource(R.drawable.dice5)
            }else if (number1 == 6) {
                diceImage1.setImageResource(R.drawable.dice6)
            }

            if (number2 == 1) {
                diceImage2.setImageResource(R.drawable.dice1)
            } else if (number2 == 2) {
                diceImage2.setImageResource(R.drawable.dice2)
            }else if (number2 == 3) {
                diceImage2.setImageResource(R.drawable.dice3)
            }else if (number2 == 4) {
                diceImage2.setImageResource(R.drawable.dice4)
            }else if (number2 == 5) {
                diceImage2.setImageResource(R.drawable.dice5)
            }else if (number2 == 6) {
                diceImage2.setImageResource(R.drawable.dice6)
            }

        }
    }
}