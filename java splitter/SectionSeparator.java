import com.opencsv.CSVWriter;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class SectionSeparator {

public void  separate(String filePath,String targetPath) throws IOException

{


    ArrayList<ArrayList<String>> contentListRL = new ArrayList<ArrayList<String>>();
    ArrayList<ArrayList<String>> contentListLL = new ArrayList<ArrayList<String>>();
    ArrayList<ArrayList<String>> contentListT = new ArrayList<ArrayList<String>>();

    BufferedReader br = new BufferedReader(new FileReader(filePath));

    String line;
    while ((line = br.readLine()) != null) {
        ArrayList<String> relevantListRL = new ArrayList<String>();
        ArrayList<String> relevantListLL = new ArrayList<String>();
        ArrayList<String> relevantListT = new ArrayList<String>();
        String[] tokens = line.split(",");

        for(int a=0;a<=8;a++)
        {
            relevantListT.add(tokens[a]);
        }
        contentListT.add(relevantListRL);
        for(int a=27;a<=35;a++)
        {
          relevantListRL.add(tokens[a]);
        }
        contentListRL.add(relevantListRL);



        for(int a=36;a<=44;a++)
        {
            relevantListLL.add(tokens[a]);
        }
        contentListLL.add(relevantListLL);

    }

    File file = new File(targetPath+"LL.csv");
    file.getParentFile().mkdirs();
    writeToCSV(contentListLL,file,targetPath);

     file = new File(targetPath+"RL.csv");
    writeToCSV(contentListRL,file,targetPath);
    file = new File(targetPath+"T.csv");
    writeToCSV(contentListRL,file,targetPath);

}


private void writeToCSV(ArrayList<ArrayList<String>>contentList,File file,String targetPath )
{

    try {

        // create FileWriter object with file as parameter
        FileWriter outputfile = new FileWriter(file);

        // create CSVWriter object filewriter object as parameter
        CSVWriter writer = new CSVWriter(outputfile);

        // adding header to csv
        String[] header = { "xacc", "yacc", "zacc","xacc","zacc","data6","xacc","yacc","zacc" };
        writer.writeNext(header);



        for(int i=0;i<=124;i++)
        {
            String[] currentArray = contentList.get(i).toArray(new String[0]);
            writer.writeNext(currentArray);
        }


        // closing writer connection
        writer.close();





    }
    catch (IOException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
}
}


