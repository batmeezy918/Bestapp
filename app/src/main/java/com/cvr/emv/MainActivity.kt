package com.cvr.emv

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

/**
 * CVR EMV Android client.
 * MIR-aligned visualization surface for Virtual Card / Terminal / APDU timeline.
 * Build is driven exclusively by tools/cvr.py → android.package node.
 */
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
