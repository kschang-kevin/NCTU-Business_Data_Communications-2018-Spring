using System;
using System.Collections.Generic;
using System.Web;
using System.Web.Services;
using System.IO;
using System.Text;
using System.Net;
namespace exchange_rate
{
    public class crawler
    {
        public static string gethtml(string url)
        {
            //處理內容  
            string html = "";
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "GET";
            request.Accept = "*/*"; //接受任意檔案
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)"; // 模擬使用IE在瀏覽 http://www.52mvc.com
            request.AllowAutoRedirect = true;//是否允許302
            request.CookieContainer = new CookieContainer();//cookie容器，
            request.Referer = url; //當前頁面的引用
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream stream = response.GetResponseStream();
            StreamReader reader = new StreamReader(stream, Encoding.Default);
            html = reader.ReadToEnd();
            stream.Close();
            return html;
        }
    }
    /// <summary>
    ///WebService1 的摘要描述
    /// </summary>
    [WebService(Namespace = "http://0516045/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {
        [WebMethod]
        public string Rate()
        {
            int i;
            string html_content = "";
            string change_rate = "";
            html_content = exchange_rate.crawler.gethtml("https://rate.bot.com.tw/xrt/fltxt/0/day");
            for(i=0;i<html_content.Length;i++)
            {
                if (Convert.ToInt32(html_content[i])>=65 && Convert.ToInt32(html_content[i]) <= 90)
                {
                    change_rate += html_content[i];
                    change_rate += html_content[i + 1];
                    change_rate += html_content[i + 2];
                    change_rate += ' ';
                    change_rate += html_content[i + 21];
                    change_rate += html_content[i + 22];
                    change_rate += html_content[i + 23];
                    change_rate += html_content[i + 24];
                    change_rate += html_content[i + 25];
                    change_rate += html_content[i + 26];
                    change_rate += html_content[i + 27];
                    change_rate += html_content[i + 28];
                    change_rate += '\n';
                    i += 17;
                }
            }
            change_rate += "TWD 1.00000\n";
            return change_rate;
        }
        [WebMethod]
        public double exchange_rate_between_different_dollar(string a,string b)
        {
            int i;
            string rate_a="", rate_b="";
            string html_content = "";
            html_content = exchange_rate.crawler.gethtml("https://rate.bot.com.tw/xrt/fltxt/0/day");
            for (i = 0; i < html_content.Length; i++)
            {
                if (html_content[i]==a[0]&& html_content[i+1] == a[1] && html_content[i+2] == a[2] )
                {
                    rate_a += html_content[i + 21];
                    rate_a += html_content[i + 22];
                    rate_a += html_content[i + 23];
                    rate_a += html_content[i + 24];
                    rate_a += html_content[i + 25];
                    rate_a += html_content[i + 26];
                    rate_a += html_content[i + 27];
                    rate_a += html_content[i + 28];
                }
                if (html_content[i] == b[0] && html_content[i + 1] == b[1] && html_content[i + 2] == b[2])
                {
                    rate_b += html_content[i + 21];
                    rate_b += html_content[i + 22];
                    rate_b += html_content[i + 23];
                    rate_b += html_content[i + 24];
                    rate_b += html_content[i + 25];
                    rate_b += html_content[i + 26];
                    rate_b += html_content[i + 27];
                    rate_b += html_content[i + 28];
                }
            }
            if(a=="TWD")
            {
                rate_a += "1";
            }
            if (b == "TWD")
            {
                rate_b += "1";
            }
            double rate_a_float = Convert.ToDouble(rate_a);
            double rate_b_float = Convert.ToDouble(rate_b);
            return rate_a_float / rate_b_float;
        }
    }
}
