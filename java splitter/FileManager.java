import java.util.ArrayList;
import java.util.Arrays;

public class FileManager {

    private ArrayList<String> actions = new ArrayList<String>(Arrays.asList("bike","jumping","running","sitting","standing","stepper","walking"));
    private ArrayList<String> subfolders = new ArrayList<String>(Arrays.asList("p1","p2","p3","p4","p5","p6","p7","p8"));
    public ArrayList<String> generateFilePaths()
    {
        ArrayList<String> paths = new ArrayList<String>();


        String initial = "D:\\WiSE2018\\Signal Processing\\data";
        for (String action : actions) {

            for (String subfolder : subfolders) {
                for(int i = 1;i<=9;i++)
                {
                    paths.add(initial+"\\"+action+"\\"+subfolder+"\\"+"s0"+i+".txt");

                }
                for(int i = 10;i<=60;i++)
                {
                    paths.add(initial+"\\"+action+"\\"+subfolder+"\\"+"s"+i+".txt");

                }

            }

        }


        return paths;
    }

    public ArrayList<String> generateTargetPaths()
    {
        ArrayList<String> paths = new ArrayList<String>();


        String initial = "D:\\WiSE2018\\Signal Processing\\isolatedData";

        for (String action : actions) {

            for (String subfolder : subfolders) {
                for(int i = 1;i<=9;i++)
                {
                    paths.add(initial+"\\"+action+"\\"+subfolder+"\\"+"s0"+i);

                }
                for(int i = 10;i<=60;i++)
                {
                    paths.add(initial+"\\"+action+"\\"+subfolder+"\\"+"s"+i);

                }

            }

        }

        return paths;
    }


}
