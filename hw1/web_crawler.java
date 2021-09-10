import java.io.*;
import java.net.*;

public class web_crawler 
{
	public static void gettitle() throws Exception 
   	{
   		int i,j,k;
		String result="";
		URL url = new URL("https://www.iim.nctu.edu.tw");
		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		conn.setRequestMethod("GET");
		BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
		String line;
		while ((line = rd.readLine()) != null) 
		{
		   result=result+line;
		}
		char[] pageContent = result.toCharArray();
		for(i=0;i<pageContent.length;i++)
		{
			if(pageContent[i]=='<'&&pageContent[i+1]=='t'&&pageContent[i+2]=='i'&&pageContent[i+3]=='t'&&pageContent[i+4]=='l'&&pageContent[i+5]=='e'&&pageContent[i+6]=='>')
			{
				for(j=0;j<pageContent.length;j++)
				{
					if(pageContent[j]=='<'&&pageContent[j+1]=='/'&&pageContent[j+2]=='t'&&pageContent[j+3]=='i'&&pageContent[j+4]=='t'&&pageContent[j+5]=='l'&&pageContent[j+6]=='e'&&pageContent[j+7]=='>')
					{
						for(k=i;k<j+8;k++)
						{
							System.out.print(pageContent[k]);
						}
						System.out.print("\n");			
					}
				}
			}		
		}
      rd.close();
      
   }

	public static void main(String[] args) throws Exception
	{
		gettitle();
	}
}