using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player
{
    static void Main(string[] args)
    {
        int boxCount = int.Parse(Console.ReadLine());

        List<Box> boxes = new List<Box>();

        float totalWeight = 0;
        for (int i = 0; i < boxCount; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            float weight = float.Parse(inputs[0]);
            float volume = float.Parse(inputs[1]);
            boxes.Add(new Box(i, volume, weight));
            totalWeight+=weight;
        }

        float idealWeightPerTruck = totalWeight/100;
        string bestResult = "";
        float maxDiff = -1;

        for (int i = 0; i<100000;i++)
        {
            float diff;
            float min = -1;
            float max = -1;

            List<Truck> result = Distribute(boxes);
            foreach(Truck t in result)
            {
                if ((min == -1) && (max == -1))
                {
                    min = t.weight;
                    max = t.weight;
                }
                else
                {
                    if (min > t.weight)
                    {
                        min = t.weight;
                    }
                    else if (max < t.weight)
                    {
                        max = t.weight;
                    }
                }
            }
            diff = max-min;
            if ((diff < maxDiff) || (maxDiff == -1))
            {
                bestResult = result[0].result;
                maxDiff = diff;
            }
        }



        // Write an action using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(bestResult); // number of truck in which box is placed
    }

    static List<Truck> Distribute(List<Box> boxes)
    {
        List <Truck> trucks = new List<Truck>();
        for(int i = 0;i < 100; i++)
        {
            trucks.Add(new Truck(i, 100, 0));
        }

        Random r = new Random();
        foreach (Box b in boxes)
        {
            if (trucks[0].result != "")
                trucks[0].result += " ";
            int rInt = r.Next(0, 99);
            while (trucks[rInt].volume < b.volume)
                rInt = r.Next(0, 99);

            trucks[rInt].volume = trucks[rInt].volume - b.volume;
            trucks[rInt].contents.Add(b.id);
            trucks[0].result += rInt.ToString();
        }
        return trucks;
    }

    class Truck
    {
        public int id;
        public float volume;
        public float weight;

        public string result = "";

        public List<int> contents;

        public Truck(int id, float volume, float weight)
        {
            this.id = id;
            this.volume = volume;
            this.weight = weight;
            contents = new List<int>();
        }
    }

    class Box
    {
        public int id;
        public float volume;
        public float weight;

        public Box(int id, float volume, float weight)
        {
            this.id = id;
            this.volume = volume;
            this.weight = weight;
        }
    }
}