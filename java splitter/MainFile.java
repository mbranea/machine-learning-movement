import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

public class MainFile {


    public static void main(String[] args) throws IOException {
        SectionSeparator separator = new SectionSeparator();
        FileManager manager = new FileManager();

        ArrayList<String> filePaths = manager.generateFilePaths();
        ArrayList<String> targetPaths = manager.generateTargetPaths();


        Iterator<String> it1 = filePaths.iterator();
        Iterator<String> it2 = targetPaths.iterator();

        while (it1.hasNext() && it2.hasNext()) {
          separator.separate(it1.next(),it2.next());
        }

    }
}
