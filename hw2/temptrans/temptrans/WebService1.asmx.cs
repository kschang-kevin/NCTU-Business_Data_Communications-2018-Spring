using System;
using System.Collections.Generic;
using System.Web;
using System.Web.Services;

namespace temptrans
{
    /// <summary>
    ///WebService1 的摘要描述
    /// </summary>
    [WebService(Namespace = "http://temperature.change/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]

    public class WebService1 : System.Web.Services.WebService
    {

        [WebMethod]
        public double FtoC(double F)
        {
            return (F - 32) * 5 / 9;
        }
        [WebMethod]
        public double CtoF(double C)
        {
            return C * 9 / 5 + 32;
        }
        [WebMethod]
        public double FtoK(double F)
        {
            return (F - 32) * 5 / 9+273.15;
        }
        [WebMethod]
        public double CtoK(double C)
        {
            return C+273.15;
        }
        [WebMethod]
        public double KtoC(double K)
        {
            return K-273.15;
        }
        [WebMethod]
        public double KtoF(double K)
        {
            return (K+273.15) * 9 / 5 + 32;
        }
    }
}
