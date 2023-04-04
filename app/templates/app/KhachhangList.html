<%@page import="Model.Bean.Trasua"%>
<%@page import="Model.Bean.Admin"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Menu</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        #main{
            display: flex;padding:20px;margin-top:180px;
        }
        #sidebar{
            width: 22%;
            height: 100%;
        }
        #content {
            width: 78%;
            height: 530px;
            border: 2px solid #007bff;
            padding: 10px 20px;
            margin-left:30px ;
            overflow-y: scroll;
        }
        #navbar{
            position: fixed;top: 0;width: 100%;height: 180px;z-index: 10;
        }
        <% if (request.getSession().getAttribute("account")==null) { %>
        .session {
        	display: none !important;
        }	
        <% } %>
        <% 
        if (request.getSession().getAttribute("account")!=null) {
        	if (!((Admin) request.getSession().getAttribute("account")).getRoles().equals("KH")) {
        %>
		        .sessionKH {
		        	display: none !important;
		        }	
        <% 
        	}
        } 
        %>
        <% 
        if (request.getSession().getAttribute("account")!=null) {
        	if (!((Admin) request.getSession().getAttribute("account")).getRoles().equals("AD")) {
        %>
		        .sessionAD {
		        	display: none !important;
		        }	
        <% 
        	}
        } 
        %>
    </style>
</head>
<body>
	<div id="navbar">
        <jsp:include page="Nav.jsp" ></jsp:include>
    </div>
    <div id="main">
        <div id="sidebar">
            <jsp:include page="Sidebar.jsp" ></jsp:include>
        </div>
        <div id="content" style="background-image: url('image/BG.png');">
            <h4 style="width:100%;text-align:center;color:#007bff;margin-top:20px;">Danh sách khách hàng</h4>
            <form action="Khachhang?deleteall=1" method="post">
	            <table width='100%' class="table table-striped">
	                <thead>
	                    <tr>
	                        <th scope="col">Username</th>
	                        <th scope="col">Password</th>
	                        <th scope="col">First name</th>
	                        <th scope="col">Last name</th>
	                        <th scope="col">Address</th>
	                        <th scope="col">SDT</th>
	                        <th scope="col" class="session sessionAD">Action</th>
	                        <th scope="col" class="sessionAD session">Choose</th>
	                    </tr>
	                </thead>
	                <tbody>
	                    <%
	                    ArrayList<Admin> listKH = (ArrayList<Admin>)request.getAttribute("listKH");
	                    for (int i=0; i<listKH.size(); i++) {
	                    %>
	                    <tr>
	                    	<td><%= listKH.get(i).getUser() %></td>
	                    	<td><%= listKH.get(i).getPass() %></td>
	                    	<td><%= listKH.get(i).getFirstname()%></td>
	                    	<td><%= listKH.get(i).getLastname() %></td>
	                    	<td><%= listKH.get(i).getAddress() %></td>
	                    	<td><%= listKH.get(i).getSdt() %></td>
	                    	<td  class="session"> 
	                    	<a class="sessionAD" href="Khachhang?delete=<%=listKH.get(i).getUser() %>"><button type="button" class="btn btn-primary" onclick="return confirm('Are you sure you want to delete?')">Delete</button></a></td>
	                   		<td class="sessionAD session"><input type="checkbox" name="<%= listKH.get(i).getUser() %>" /></td>
	                   	</tr>
	                   	<% 
	                   	}
	                   	%>
	                </tbody>        
	            </table>
	            <button type="submit" class="session btn btn-primary sessionAD" style="margin-left:auto;display:block;" 
	            onclick="return confirm('Are you sure you want to delete all?')">Delete All</button>
            </form>
        </div>
    </div>
</body>
</html>