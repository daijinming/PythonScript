FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY . ./aspnetapp/

# copy everything else and build app

WORKDIR /app/aspnetapp

RUN dotnet restore

RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS runtime
WORKDIR /app

COPY --from=build /app/aspnetapp/out ./

ENTRYPOINT ["dotnet", "appdemo1.dll"]

