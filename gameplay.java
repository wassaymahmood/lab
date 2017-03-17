package com.example.wassay.asignment;

import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Rect;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;



import java.util.Random;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.SurfaceHolder;
import android.view.SurfaceView;

public class gameplay extends Activity {

    MySurfaceView mySurfaceView;

    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mySurfaceView = new MySurfaceView(this);
        setContentView(mySurfaceView);
    }

    @Override
    protected void onResume() {
        // TODO Auto-generated method stub
        super.onResume();
        mySurfaceView.onResumeMySurfaceView();
    }

    @Override
    protected void onPause() {
        // TODO Auto-generated method stub
        super.onPause();
        mySurfaceView.onPauseMySurfaceView();
    }

    class MySurfaceView extends SurfaceView implements Runnable {

        Thread thread = null;
        SurfaceHolder surfaceHolder;
        volatile boolean running = false;

        private Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        Random random;

        public MySurfaceView(Context context) {
            super(context);
            // TODO Auto-generated constructor stub
            surfaceHolder = getHolder();
            random = new Random();
        }

        public void onResumeMySurfaceView() {
            running = true;
            thread = new Thread(this);
            thread.start();
        }

        public void onPauseMySurfaceView() {
            boolean retry = true;
            running = false;
            while (retry) {
                try {
                    thread.join();
                    retry = false;
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }

        @Override
        public void run() {
            // TODO Auto-generated method stub
            while (running) {
                if (surfaceHolder.getSurface().isValid()) {
                    Canvas canvas = surfaceHolder.lockCanvas();
                    //... actual drawing on canvas

                    paint.setStyle(Paint.Style.STROKE);
                    paint.setStrokeWidth(3);
                    paint.setColor(0xFFFFFFFF);

                    Bitmap snake;
                    int w = canvas.getWidth();
                    int h = canvas.getHeight() - 280;
                    int a = 0;
                    int t = 0;
                    int b = 110;



                    for (int z = 0; z <= w; z += w * 1 / 10) {

                        for (int p = 0; p <= h; p += h * 1 / 10) {

                            canvas.drawRect(t, a, z, p, paint);
                            paint.setTextSize(96);
                            canvas.drawText(String.valueOf(b), z, p, paint);
                            b = b - 10;
                        }
                        b = b + 109;
                    }

                    Bitmap s1 = BitmapFactory.decodeResource(getResources(), R.drawable.s);
                    Bitmap s4 = BitmapFactory.decodeResource(getResources(), R.drawable.s1);
                    Bitmap s2 = BitmapFactory.decodeResource(getResources(), R.drawable.ladder);
                    Bitmap s3 = BitmapFactory.decodeResource(getResources(), R.drawable.ladder);
                    canvas.drawBitmap(s2, 20,50 ,paint);
                    canvas.drawBitmap(s3, 890,780 ,paint);
                    canvas.drawBitmap(s1, 10,950 ,paint);
                    canvas.drawBitmap(s4, 880,15 ,paint);

                    surfaceHolder.unlockCanvasAndPost(canvas);

                }
            }
        }

    }
}


