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
            <h4 style="width:100%;text-align:center;color:#007bff;margin-top:20px;">Danh sách trà sữa</h4>
            <form action="Trasua?buyall=1" method="post">
	            <table width='100%' class="table table-striped">
	                <thead>
	                    <tr>
	                        <th scope="col">ID</th>
	                        <th scope="col">Type</th>
	                        <th scope="col">Size</th>
	                        <th scope="col">Money</th>
	                        <th scope="col" class="session">Action</th>
	                        <th scope="col" class="sessionKH">Choose</th>
	                    </tr>
	                </thead>
	                <tbody>
	                    <%
	                    ArrayList<Trasua> listTS = (ArrayList<Trasua>)request.getAttribute("listTS");
	                    for (int i=0; i<listTS.size(); i++) {
	                    %>
	                    <tr>
	                    	<td><%= listTS.get(i).getId() %></td>
	                    	<td><%= listTS.get(i).getLoai() %></td>
	                    	<td><%= listTS.get(i).getKichthuoc() %></td>
	                    	<td><%= listTS.get(i).getGia() %></td>
	                    	<td  class="session"> <a class="sessionAD" href="Trasua?update=<%=listTS.get(i).getId() %>"><button type="button" class="btn btn-primary">Update</button></a>
	                    	<a class="sessionKH" href="Trasua?buy=<%=listTS.get(i).getId() %>"><button type="button" class="btn btn-primary" onclick="return confirm('Are you sure you want to buy?')">Buy</button></a></td>
	                   		<td class="sessionKH"> <input type="checkbox" name="<%= listTS.get(i).getId() %>" id="<%= listTS.get(i).getId() %>" 
	                   		onclick="TongGia('<%= listTS.get(i).getGia() %>', '<%= listTS.get(i).getId() %>' )" /> </td>
	                   	</tr>
	                   	<% 
	                   	}
	                   	%>
	                </tbody>        
	            </table>
	            <label for="tonggia" class="d-inline sessionKH">Tổng giá trị: </label>
	            <input type="text" id="tonggia" class="d-inline form-control sessionKH" style="width:800px" value="0" readonly>
	            <button type="submit" class="session btn btn-primary sessionKH" style="margin-left:auto;display:block;" 
	            onclick="return confirm('Are you sure you want to buy all?')">Buy All</button>
            </form>
        </div>
    </div>
	<script>
		var tong = parseInt(document.getElementById("tonggia").value); 
        function TongGia(gia, id) {
        	var checkbox = document.getElementById(id); 
        	let gia2 = parseInt(gia); 
        	if (checkbox.checked==true) {
        		tong = tong + gia2;
        	} else {
        		tong = tong - gia2;
        	}
        	document.getElementById("tonggia").value = tong; 
        }
     </script>
</body>
</html>