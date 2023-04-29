package com.example.sd_lecture

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ListView

class ListViewActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list_view)

        val list_item = mutableListOf<ListViewModel>()

        list_item.add(ListViewModel("A", "A content"))
        list_item.add(ListViewModel("B", "B content"))
        list_item.add(ListViewModel("C", "C content"))

        val listview = findViewById<ListView>(R.id.mainListView)

        val listAdapter = ListViewAdapter(list_item)

        listview.adapter = listAdapter
    }
}