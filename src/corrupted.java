import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class corrupted {
    ArrayList<BinFile> files;

    public corrupted() {
        files = new ArrayList();
    }

    public void addFile(String name) throws FileNotFoundException {//assuming file is already in binary
        // (and numerous copies of binary files)
        files.add(new BinFile(name));
    }

    public void calc() {
        String[] major = new String[2];
        for (int ind = 0; ind < files.get(0).body.length(); ind++) {//ind of binary dig being checked
            for (int file = 0; file < files.size(); file++) {//which file being checked
                major[files.get(file).body.charAt(ind) - '0'] += file + " ";
            }
            boolean ifDiff = major[0].length() != 0 && major[1].length() != 0;
            if (ifDiff) {
                if (major[0].length() == major[1].length()) {
                    System.out.println("More sophisticated error analysis needed");
                    break;
                } else {//check which is majority
                    boolean likely = major[1].length() > major[0].length();//likely state, true = 1, false = 0
                    int numWrong = 0;
                    if (likely) {
                        while (major[0].indexOf(" ") >= 0) {
                            int wrongFile = Integer.parseInt(major[0].substring(0, major[0].indexOf(" ")));
                            files.get(wrongFile).likelyWrong[1] += ind + " ";//stores what the value should be
                            major[0] = major[0].substring(major[0].indexOf(" ") + 1);//will go till end
                            files.get(wrongFile).likelyWrong[2] += " ";
                            numWrong++;
                        }
                    } else {
                        while (major[1].indexOf(" ") >= 0) {
                            int wrongFile = Integer.parseInt(major[1].substring(0, major[1].indexOf(" ")));
                            files.get(wrongFile).likelyWrong[0] += ind + " ";//stores what the value should be
                            major[1] = major[1].substring(major[1].indexOf(" ") + 1);//will go till end
                            files.get(wrongFile).likelyWrong[2] += " ";
                            numWrong++;
                        }
                    }

                }
            }
        }

    }
}

    class BinFile {
        public String body;
        public String[] likelyWrong;

        public BinFile(String name) throws FileNotFoundException {
            Scanner s = new Scanner(new File(name));
            while (s.hasNextLine()) {
                this.body += s.nextLine();//Im unfamiliar with the structure of binary files?
            }
            likelyWrong = new String[3];//3rd bucket will be total inds
        }

        public String numIncorrect() {
            return "Number of corruptions in this file: " + likelyWrong[2].length();
        }

        //further research needed
        public String CalcAffectedAreas(){

            return "";
        }
        //

    }


//    private int whichWrong(String[] in, int curr){//curr is location of binary digit being checked
//        int numWrong = 0;
//        int right;
//
//        if(in[0].length() > in[1].length()) right = 0;//0 is likely right digit
//        else if(in[1].length() > in[0].length()) right = 1;
//        else right = -1;
//        if(right >= 0){
//            while (in[right].length() > 0) {
//                int toCorrect;
//                if (in[right].indexOf(',') > 0) {
//                    toCorrect = Integer.parseInt(in[right].substring(0, in[right].indexOf(',')));
//                    in[1] = in[1].substring(in[1].indexOf(',') + 1);
//                } else {
//                    toCorrect = Integer.parseInt(in[1]);
//                }
//                files.get(toCorrect).likelyWrong[curr] = 1;//will go till end
//                numWrong++;
//            }
//        }
//        }else if()
//
//
//
//    }

//    public void calc(){
//        int numDiff = 0;
//        for(int i = 0; i < files.get(0).body.length(); i++){//location of binary digit
//            String[] maj = new String[2];
//            maj[files.get(0).body.charAt(i) - '0'] += 0 + " ";
//            for(int i2 = 1; i2 < files.size(); i2++){//check if same digit in multiple files
//                boolean majState = maj[1].length() > maj[0].length();//if lengths are equal???
//                ifSame = files.get(0).body.charAt(i) == files.get(i2).body.charAt(i);
//                maj[files.get(i2).body.charAt(i) - '0'] += i2 + " ";//actual number of indices will be # of spaces in string
//            }
//        }
//
//    }


